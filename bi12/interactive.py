# -*- coding: utf-8 -*-
from bi12 import part
from bi12 import bible
from bi12 import __version__


def start():
    while True:
        command = _prompt(' bi12 > ')
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


def _prompt(ent=' bi12 > '):
    try:
        result = input(ent).lower()
        return result
    except (KeyboardInterrupt, EOFError):
        return 'exit'
