#!python3
'''
moncode - Format code for MongoDB slides.
'''

import io
from itertools import groupby
import logging
import textwrap
from sys import stdin, stdout

import click
from pygments.lexers import get_lexer_by_name, guess_lexer, guess_lexer_for_filename
from pygments import highlight
from pygments.lexers import Python2Lexer, PythonLexer, get_all_lexers
from pygments.formatters import HtmlFormatter, RtfFormatter
import pyperclip

from .styles import MongoDark

@click.group()
def main():
    '''
    moncode - Format code for MongoDB slides.
    '''
    logging.basicConfig(format="%(message)s")

@main.command()
@click.option('-l', '--language', help="""The programming language to be formatted.
If not supplied, this will be guessed from the file name or content.
It's better to supply it if you can. Run `moncode languages` to see a list of supported input languages.""")
@click.option('-i', '--input', type=click.File(), help="The path to a code file to be formatted. If not supplied, either code will be read from stdin, or else copied from the clipboard.")
@click.option('-o', '--output', type=click.File('w'), help="The path to write output to.")
@click.option('-f', '--format', type=click.Choice(['html', 'rtf']), default='rtf', help="The output format. Defaults to 'rtf' (which is good for copy-pasting).")
@click.option('-q', '--quiet', 'verbosity', flag_value=0, help="Run quietly.")
@click.option('-v', '--verbose', 'verbosity', flag_value=2, help="Run loudly.")
def format(language=None, input=None, format=None, output=None, verbosity=None):
    '''
    Format code for MongoDB slides.

    \b
    # Copy code from the clipboard, format it as RTF and then copy the result to the clipboard.
    moncode format

    \b
    # Specify the language if a guess is wrong:
    moncode format --language ruby

    \b
    # Read code from stdin and copy result to clipboard:
    cat sample_inputs/sample.js | moncode

    \b
    # Read from sample.py and write to output.rtf:
    moncode -i sample.py -o output.rtf

    \b
    # Read from the clipboard, and write to stdout:
    moncode -o -
    '''

    logging.getLogger().setLevel({
        None: logging.INFO,
        0: logging.WARNING,
        2: logging.DEBUG,
    }[verbosity])
    
    code = None
    if input:
        logging.debug("Input from file: %s", input.name)
        code = input.read()
    # If stdin is not a tty, then code is being piped in:
    elif not stdin.isatty():
        logging.debug("Input from stdin")
        code = stdin.read()
    else:
        logging.debug("Input from clipboard")
        code = pyperclip.paste()

    # Remove any common whitespace prefix:
    code = textwrap.dedent(code)

    lexer = None
    lexer_args = {
        'stripall': True,
        'tabsize': 4,
    }
    if language:
        logging.debug("Language specified: %s", language)
        lexer = get_lexer_by_name(language, **lexer_args)
    else:
        if input:
            logging.debug("Language guessed from filename %s", input.name)
            lexer = guess_lexer_for_filename(input.name, code, **lexer_args)
        else:
            logging.debug("Language guessed from content")
            lexer = guess_lexer(code, **lexer_args)

    # The Python2 lexer appears to return a higher confidence than the Python3 lexer.
    # Fix this abomination:
    if isinstance(lexer, Python2Lexer):
        lexer = PythonLexer(**lexer_args)
    
    logging.debug("Lexer: %r", lexer.name)
    logging.debug("Output format: %s", format)
    
    output_func = globals()[f'output_{format}']

    if output:
        logging.debug("Output written to %s", output.name)
        output_func(output, code, lexer)
    else:
        logging.info("Output written to clipboard")
        buffer = io.StringIO()
        output_func(buffer, code, lexer)
        pyperclip.copy(buffer.getvalue())


def lexer_names():
    for name, aliases, filenames, mimetypes in get_all_lexers():
        yield aliases[0]


@main.command()
def languages():
    '''
    List all the input languages supported by moncode.
    '''
    for _, names in groupby(sorted(lexer_names()), lambda name: name[0]):
        print(', '.join(names))


def output_rtf(f, code, lexer):
    # Font size is specified in HALF POINTS; 28 = 14pt
    formatter = RtfFormatter(style=MongoDark, fontface="fira mono", fontsize=37)
    f.write(highlight(code, lexer, formatter))


def output_html(f, code, lexer):
    formatter = HtmlFormatter(noclasses=False, style=MongoDark)
    f.write("""
    <!doctype html>
    <html>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        div.highlight pre {
            font-family: "fira mono";
            font-size: 14pt;
        }
        div.highlight {
            color: #65C9DF;
            background-color: #21313c;
        }

        """
        + formatter.get_style_defs()  +
        """        

    </style>
    <body>
    """)
    f.write(highlight(code, lexer, formatter))
    f.write("""
    </body>
    </html>
    """)


if __name__ == '__main__':
    main()
