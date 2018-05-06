# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter

from bi12 import printer
from bi12 import parse
from bi12 import __version__


def start():
    while True:
        command = _prompt(' bi12 > ')
        cmd = command.split(" ")
        # bi book
        parser = parse.bibleParse()
        parser.parse(command)
        # command
        if parser.chapter != []:
            print(parser.book.capitalize())
            for i, chap in enumerate(parser.chapter):
                printer.parter(parser.book, chap, parser.verset2[i])
        elif cmd[0] == "exit":
            break
        elif cmd[0] == "quit":
            break
        elif cmd[0] == "version":
            print("Version:", __version__)


book = WordCompleter(parse.bookList)


def _prompt(ent=' bi12 > '):
    try:
        result = prompt(ent,
                        completer=book).lower()
        return result
    except (KeyboardInterrupt, EOFError):
        return 'exit'
