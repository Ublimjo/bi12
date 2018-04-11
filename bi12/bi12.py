#!/data/data/com.termux/files/usr/bin/env python

"""
bi12 - entry point for called in /usr/bin/
"""

import sys
import click

from bi12 import bible
from bi12 import part

__version__ = "0.6"


@click.command()
def main():
    """
        bi12 - Bible new world translation(NWT) in pure python
    """
    print("===========================================")
    print("  Baiboly fandikan-teny ny tontolo vaovao")
    print("    Version :", __version__)
    print("===========================================")
    while True:
        command = input(" bi12 > ").lower()
        cmd = command.split(" ")
        # bi book
        parser = bible.bibleParse()
        parser.parse(command)
        if parser.chapter != []:
            print(parser.book.capitalize())
            for i, chap in enumerate(parser.chapter):
                part.parter(parser.book, chap, parser.verset2[i])
        elif cmd[0] == "exit":
            break
        elif cmd[0] == "quit":
            break
        elif cmd[0] == "version":
            print("Version:", __version__)


def view(command):
    """
        view function called for non-interactive mode
    """
    command = command.lower()
    parser = bible.bibleParse()
    parser.parse(command)
    if parser.chapter != 0:
        part.parter(parser.book, parser.chapter, parser.verset2)
