# -*- coding: utf-8 -*-
import sys
import click

from bi12 import __version__


@click.command()
def main():
    """
        bi12 - Bible new world translation(NWT) in pure python
    """
    greetings()
    from bi12 import interactive
    sys.exit(interactive.start())


def greetings():
    import os
    print('=' * os.get_terminal_size()[0])
    print("  Baiboly fandikan-teny ny tontolo vaovao")
    print("    Version :", __version__)
    print('=' * os.get_terminal_size()[0])
