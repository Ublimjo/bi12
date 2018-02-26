import edit_distance as ed
bookList = ["genesisy", "eksodosy", "levitikosy", "nomery", "deoteronomia", "josoa", "mpitsara", "rota", "1 samoela", "2 samoela", "1 mpanjaka", "2 mpanjaka", "1 tantara", "2 tantara", "ezra", "nehemia", "estera", "joba", "salamo", "ohabolana", "mpitoriteny", "tononkiran’i solomona", "isaia", "jeremia", "fitomaniana", "ezekiela", "daniela", "hosea", "joela", "amosa", "obadia", "jona", "mika", "nahoma", "habakoka", "zefania", "hagay", "zakaria", "malakia", "matio", "marka", "lioka", "jaona", "asan’ny apostoly", "romanina", "1 korintianina", "2 korintianina", "galatianina", "efesianina", "filipianina", "kolosianina", "1 tesalonianina", "2 tesalonianina", "1 timoty", "2 timoty", "titosy", "filemona", "hebreo", "jakoba", "1 petera", "2 petera", "1 jaona", "2 jaona", "3 jaona", "joda", "apokalypsy"]


def parseInt(enter):
	try:
		return int(enter)
	except:
		return 0

class bibleParse:
	def __init__(self):
		self.book = ""
		self.raw_verset = ""
		self.verset1 = 0
		self.raw_verset2 = ""
		self.verset2 = []

	def parse(self, enter):
	# -- test book
		cmd = enter.lower().split(" ")
		if len(cmd) == 1:
			return False

		prebook1 = (cmd[0] + " " + cmd[1])
		prebook2 = (cmd[0])
		solver = ed.EditDistance()

		if (prebook1) in bookList:
			entbook = cmd[0] + " " + cmd[1]
			withSub = True
		elif (prebook2) in bookList:
			entbook = cmd[0]
			withSub = False
		else:
			for ix in bookList:
				if solver.solve(prebook1, ix) <= 2:
					entbook = ix
					withSub = True
				elif solver.solve(prebook2, ix) <= 2:
					entbook = ix
					withSub = False
	# -- test verset
		if not withSub:
			verset = cmd[1].split(":")[0]
			subverset = cmd[1].split(":")[1].split(",")
		else:
			verset = cmd[2].split(":")[0]
			subverset = cmd[2].split(":")[1].split(",")
		
		# convert "Matio 24:14-17" to "Matio 24:14,15,16,17"
		for i, lsvt in enumerate(subverset):
			if "-" in str(lsvt):
				del subverset[i]
				a = int(lsvt.split("-")[0])
				z = int(lsvt.split("-")[1])
				while a <= z:
					subverset.insert(i, a)
					a += 1
					i += 1
		
	#activate
		self.book = entbook
		self.raw_verset = verset+":"+str(subverset)
		self.verset1 = verset
		self.raw_verset2 = subverset
		self.verset2 = subverset
		
		