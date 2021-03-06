# -*- coding: utf-8 -*-
from bi12 import color

import hues
import textwrap
from bs4 import BeautifulSoup

bookList = [
    ["genesisy", "006_B12_.GE"],
    ["eksodosy", "007_B12_.EX"],
    ["levitikosy", "008_B12_.LE"],
    ["nomery", "009_B12_.NU"],
    ["deoteronomia", "010_B12_.DE"],
    ["josoa", "011_B12_.JOS"],
    ["mpitsara", "012_B12_.JG"],
    ["rota", "013_B12_.RU"],
    ["1 samoela", "014_B12_.1SA"],
    ["2 samoela", "015_B12_.2SA"],
    ["1 mpanjaka", "016_B12_.1KI"],
    ["2 mpanjaka", "017_B12_.2KI"],
    ["1 tantara", "018_B12_.1CH"],
    ["2 tantara", "019_B12_.2CH"],
    ["ezra", "020_B12_.EZR"],
    ["nehemia", "021_B12_.NE"],
    ["estera", "022_B12_.ES"],
    ["joba", "023_B12_.JOB"],
    ["salamo", "024_B12_.PS"],
    ["ohabolana", "025_B12_.PR"],
    ["mpitoriteny", "026_B12_.EC"],
    ["tononkiran’i solomona", "027_B12_.CA"],
    ["isaia", "028_B12_.ISA"],
    ["jeremia", "029_B12_.JER"],
    ["fitomaniana", "030_B12_.LA"],
    ["ezekiela", "031_B12_.EZE"],
    ["daniela", "032_B12_.DA"],
    ["hosea", "033_B12_.HOS"],
    ["joela", "034_B12_.JOE"],
    ["amosa", "035_B12_.AM"],
    ["obadia", "036_B12_.OB"],
    ["jona", "037_B12_.JON"],
    ["mika", "038_B12_.MIC"],
    ["nahoma", "039_B12_.NAH"],
    ["habakoka", "040_B12_.HAB"],
    ["zefania", "041_B12_.ZEP"],
    ["hagay", "042_B12_.HAG"],
    ["zakaria", "043_B12_.ZEC"],
    ["malakia", "044_B12_.MAL"],
    ["matio", "045_B12_.MT"],
    ["marka", "046_B12_.MR"],
    ["lioka", "047_B12_.LU"],
    ["jaona", "048_B12_.JOH"],
    ["asan’ny apostoly", "049_B12_.AC"],
    ["romanina", "050_B12_.RO"],
    ["1 korintianina", "051_B12_.1CO"],
    ["2 korintianina", "052_B12_.2CO"],
    ["galatianina", "053_B12_.GA"],
    ["efesianina", "054_B12_.EPH"],
    ["filipianina", "055_B12_.PHP"],
    ["kolosianina", "056_B12_.COL"],
    ["1 tesalonianina", "057_B12_.1TH"],
    ["2 tesalonianina", "058_B12_.2TH"],
    ["1 timoty", "059_B12_.1TI"],
    ["2 timoty", "060_B12_.2TI"],
    ["titosy", "061_B12_.TIT"],
    ["filemona", "062_B12_.PHM"],
    ["hebreo", "063_B12_.HEB"],
    ["jakoba", "064_B12_.JAS"],
    ["1 petera", "065_B12_.1PE"],
    ["2 petera", "066_B12_.2PE"],
    ["1 jaona", "067_B12_.1JO"],
    ["2 jaona", "068_B12_.2JO"],
    ["3 jaona", "069_B12_.3JO"],
    ["joda", "070_B12_.JUD"],
    ["apokalypsy", "071_B12_.RE"],
]


def getFileName(book):
    nbr = 0
    while nbr < 66:
        if book == bookList[nbr][0]:
            return bookList[nbr][1]

        nbr += 1


def wrap(string):
    text = textwrap.wrap(string, 40)
    line = "\n" + color.green(" | ")
    final = line.join(text) + line
    return final


def parter(book, ver1, ver2):
    """
        Function to print bible verset From file
        Matio 24:14
        :param book: 'Matio'
        :param ver1: '24'
        :param ver2: '14'
    """
    filename = getFileName(book)
    # open file
    filepath = "/data/data/com.termux/files/usr/share/bi12/FloatingBible/bi12_MG/OEBPS/"
    try:
        if int(ver1) == 1:
            filexht = open(filepath + filename + ".xhtml", "r")
        else:
            filexht = open(filepath + filename +
                           "-split" + ver1 + ".xhtml", "r")
    except FileNotFoundError:
        hues.error("File not found")
        hues.error("Invalid chapter: " + ver1)
        return False

    # parse file
    soup = BeautifulSoup(filexht, "html.parser")
    print(color.green("[" + ver1 + "]"), ver2)
    # for multiples verset
    for sver2 in ver2:
        sver2 = str(sver2)
        vrs = u"chapter" + ver1 + "_verse" + sver2
        try:
            stringPart = soup.find(
                "span", attrs={"id": vrs}).next.next.next.next
        except AttributeError:
            hues.error("Invalid verset: " + sver2)
            break
        # last print to show verset
        print(
            color.green(" | ") + color.blue("[" + sver2 + "]"),
            wrap(stringPart),
        )
