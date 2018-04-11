from bi12 import edit_distance as ed

bookList = [
    "genesisy",
    "eksodosy",
    "levitikosy",
    "nomery",
    "deoteronomia",
    "josoa",
    "mpitsara",
    "rota",
    "1 samoela",
    "2 samoela",
    "1 mpanjaka",
    "2 mpanjaka",
    "1 tantara",
    "2 tantara",
    "ezra",
    "nehemia",
    "estera",
    "joba",
    "salamo",
    "ohabolana",
    "mpitoriteny",
    "tononkiran’i solomona",
    "isaia",
    "jeremia",
    "fitomaniana",
    "ezekiela",
    "daniela",
    "hosea",
    "joela",
    "amosa",
    "obadia",
    "jona",
    "mika",
    "nahoma",
    "habakoka",
    "zefania",
    "hagay",
    "zakaria",
    "malakia",
    "matio",
    "marka",
    "lioka",
    "jaona",
    "asan’ny apostoly",
    "romanina",
    "1 korintianina",
    "2 korintianina",
    "galatianina",
    "efesianina",
    "filipianina",
    "kolosianina",
    "1 tesalonianina",
    "2 tesalonianina",
    "1 timoty",
    "2 timoty",
    "titosy",
    "filemona",
    "hebreo",
    "jakoba",
    "1 petera",
    "2 petera",
    "1 jaona",
    "2 jaona",
    "3 jaona",
    "joda",
    "apokalypsy",
]

def getDist(enter):
    """
		Function to test shortest distance of string
		Mitio -> Matio
		:param enter: string to test
	"""
    solver = ed.EditDistance()
    leaf = 0
    mean = []
    for book in bookList:
        mean.append(solver.solve(enter, book))
    while True:
        try:
            return [leaf, bookList[mean.index(leaf)]]

        except ValueError:
            leaf += 1


class bibleParse:

    def __init__(self):
        self.book = ""
        self.raw_verset = ""
        self.chapter = []
        self.raw_verset2 = ""
        self.verset2 = []

    def parse(self, enter):
        """
			parse verset input (Book with verset)
			:param enter: verset to parse
				>>> import bible
				>>> bi = bible.bibleParse().parse("Mitio 24:14,16-20")
				>>> bi.book
				Matio
				>>> bi.chapter
				24
				>>> bi.verset2
				[14,16,17,18,19,20]
			"""
        cmd = enter.lower().split(" ")
        if len(cmd) == 1:
            return False

        prebook1 = (cmd[0] + " " + cmd[1])
        prebook2 = (cmd[0])
        if getDist(prebook2)[0] < getDist(prebook1)[0]:
            entbook = getDist(prebook2)[1]
            withSub = False
        elif getDist(prebook1)[0] < getDist(prebook2)[0]:
            entbook = getDist(prebook1)[1]
            withSub = True
        # -- test verset
        verset = []
        subverset = []
        if not withSub:
            raw = cmd[1].split(";")
            for raws in raw:
                verset.append(raws.split(":")[0])
                subverset.append(raws.split(":")[1].split(","))
        else:
            raw = cmd[2].split(";")
            for raws in raw:
                verset.append(raws.split(":")[0])
                subverset.append(raws.split(":")[1].split(","))
        # convert "Matio 24:14-17" to "Matio 24:14,15,16,17"
        n = 0
        while n < len(subverset):
            for i, lsvt in enumerate(subverset[n]):
                if "-" in str(lsvt):
                    del subverset[n][i]
                    a = int(lsvt.split("-")[0])
                    z = int(lsvt.split("-")[1])
                    while a <= z:
                        subverset[n].insert(i, a)
                        a += 1
                        i += 1
            n += 1
        # activate
        self.book = entbook
        self.raw_verset = verset + subverset
        self.chapter = verset
        self.raw_verset2 = subverset
        self.verset2 = subverset
