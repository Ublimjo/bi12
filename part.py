import bible
from bs4 import BeautifulSoup

bookList = [["genesisy",              "006_B12_.GE"],
            ["eksodosy",              "007_B12_.EX"],
            ["levitikosy",            "008_B12_.LE"],
            ["nomery",                "009_B12_.NU"],
            ["deoteronomia",          "010_B12_.DE"],
            ["josoa",                 "011_B12_.JOS"],
            ["mpitsara",              "012_B12_.JG"],
            ["rota",                  "013_B12_.RU"],
            ["1 samoela",             "014_B12_.1SA"],
            ["2 samoela",             "015_B12_.2SA"],
            ["1 mpanjaka",            "016_B12_.1KI"],
            ["2 mpanjaka",            "017_B12_.2KI"],
            ["1 tantara",             "018_B12_.1CH"],
            ["2 tantara",             "019_B12_.2CH"],
            ["ezra",                  "020_B12_.EZR"],
            ["nehemia",               "021_B12_.NE"],
            ["estera",                "022_B12_.ES"],
            ["joba",                  "023_B12_.JOB"],
            ["salamo",                "024_B12_.PS"],
            ["ohabolana",             "025_B12_.PR"],
            ["mpitoriteny",           "026_B12_."],
            ["tononkiran’i solomona", "027_B12_."],
            ["isaia",                 "028_B12_."],
            ["jeremia",               "029_B12_."],
            ["fitomaniana",           "030_B12_."],
            ["ezekiela",              "031_B12_."],
            ["daniela",               "032_B12_."],
            ["hosea",                 "033_B12_."],
            ["joela",                 "034_B12_."],
            ["amosa",                 "035_B12_."],
            ["obadia",                "036_B12_."],
            ["jona",                  "037_B12_."],
            ["mika",                  "038_B12_."],
            ["nahoma",                "039_B12_."],
            ["habakoka",              "040_B12_."],
            ["zefania",               "041_B12_."],
            ["hagay",                 "042_B12_."],
            ["zakaria",               "043_B12_."],
            ["malakia",               "044_B12_."],
            ["matio",                 "045_B12_."],
            ["marka",                 "046_B12_."],
            ["lioka",                 "047_B12_."],
            ["jaona",                 "048_B12_."],
            ["asan’ny apostoly",      "049_B12_."],
            ["romanina",              "050_B12_."],
            ["1 korintianina",        "051_B12_."],
            ["2 korintianina",        "052_B12_."],
            ["galatianina",           "053_B12_."],
            ["efesianina",            "054_B12_."],
            ["filipianina",           "055_B12_."],
            ["kolosianina",           "056_B12_."],
            ["1 tesalonianina",       "057_B12_."],
            ["2 tesalonianina",       "058_B12_."],
            ["1 timoty",              "059_B12_."],
            ["2 timoty",              "060_B12_."],
            ["titosy",                "061_B12_."],
            ["filemona",              "062_B12_."],
            ["hebreo",                "063_B12_."],
            ["jakoba",                "064_B12_."],
            ["1 petera",              "065_B12_."],
            ["2 petera",              "066_B12_."],
            ["1 jaona",               "067_B12_."],
            ["2 jaona",               "068_B12_."],
            ["3 jaona",               "069_B12_."],
            ["joda",                  "070_B12_."],
            ["apokalypsy",            "071_B12_."]]

#test = bible.bibleParse()
#test.parse("1 Jagona 5:19")
#print("Book :", test.book)
#print("Verset :", test.verset1)
#print("Subverset :", test.verset2)

def parter(book, ver1, ver2):
	nbr = 0
	while nbr < 66:
		if book == bookList[nbr][0]:
			filename = bookList[nbr][1]
			break
		nbr += 1
		
	if ver1 == 1:
		filexht = open("/storage/emulated/0/FloatingBible/bi12_MG/OEBPS/" + filename + ".xhtml", "r")
	else:
		filexht = open("/storage/emulated/0/FloatingBible/bi12_MG/OEBPS/" + filename + "-split" + ver1 + ".xhtml", "r")
	soup = BeautifulSoup(filexht, "html.parser")
	print(soup.body)
		