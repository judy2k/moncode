#!python3
'''
moncode - Take code from the clipboard and format it for MongoDB slides.
'''

import textwrap
from sys import stdin, stdout

import click
from pygments.lexers import get_lexer_by_name, guess_lexer, guess_lexer_for_filename
from pygments import highlight
from pygments.lexers import Python2Lexer, PythonLexer
from pygments.formatters import HtmlFormatter, RtfFormatter
import pyperclip


from .styles import MongoDark

@click.command()
@click.option('-l', '--language')
@click.option('-i', '--input', type=click.File())
@click.option('-o', '--output', type=click.File('w'))
@click.option('-f', '--format', type=click.Choice(['html', 'rtf']), default='rtf')
def main(language=None, input=None, format=None, output=None):
    code = None
    if input:
        code = input.read()
    # If stdin is not a tty, then code is being piped in:
    elif not stdin.isatty():
        code = stdin.read()
    else:
        code = pyperclip.paste()

    # Remove any common whitespace prefix:
    code = textwrap.dedent(code)

    lexer = None
    lexer_args = {
        'stripall': True,
        'tabsize': 4,
    }
    if language:
        lexer = get_lexer_by_name(language, **lexer_args)
    else:
        if input:
            lexer = guess_lexer_for_filename(input.name, code, **lexer_args)
        else:
            lexer = guess_lexer(code, **lexer_args)

    # The Python2 lexer appears to return a higher confidence than the Python3 lexer.
    # Fix this abomination:
    if isinstance(lexer, Python2Lexer):
        lexer = PythonLexer(**lexer_args)
    
    output_func = globals()[f'output_{format}']

    if output:
        output_func(output, code, lexer)
    else:
        output_func(stdout, code, lexer)


def output_rtf(f, code, lexer):
    # Font size is specified in HALF POINTS; 28 = 14pt
    formatter = RtfFormatter(style=MongoDark, fontface="fira mono", fontsize=28)
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
