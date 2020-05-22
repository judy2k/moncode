#!python3
'''
moncode - Take code from the clipboard and format it for MongoDB slides.
'''

import click
from pygments.lexers import get_lexer_by_name, guess_lexer, guess_lexer_for_filename
from pygments import highlight
from pygments.lexers import Python2Lexer, PythonLexer
from pygments.formatters import HtmlFormatter
import pyperclip
from sys import stdin, stdout

from .styles import MongoDark

@click.command()
@click.argument('language', required=False)
@click.option('-i', '--input', type=click.File())
@click.option('-o', '--output', type=click.File())
@click.option('-f', '--format')
def main(language=None, input=None, format=None, output=None):
    code = None
    if input:
        code = input.read()
    # If stdin is not a tty, then code is being piped in:
    elif not stdin.isatty():
        code = stdin.read()
    else:
        code = pyperclip.paste()

    lexer = None
    lexer_args = {}
    if language:
        lexer = get_lexer_by_name(language)
    else:
        if input:
            lexer = guess_lexer_for_filename(input.name, code)
        else:
            lexer = guess_lexer(code)

    # The Python2 lexer appears to return a higher confidence than the Python3 lexer.
    # Fix this abomination:
    if isinstance(lexer, Python2Lexer):
        lexer = PythonLexer(**lexer_args)
    
    
    if output:
        output_html(output, code, lexer)
    else:
        output_html(stdout, code, lexer)


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
