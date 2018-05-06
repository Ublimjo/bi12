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
    width = os.get_terminal_size()[0]
    sVersion = 'Version: ' + __version__

    print('=' * width)
    print()
    print("Baiboly fandikan-teny ny tontolo vaovao".center(width))
    print(sVersion.center(width))
    print()
    print('=' * width)
