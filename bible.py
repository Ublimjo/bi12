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
		self.verset2 = 0

	def parse(self, enter):
	#test book
		cmd = enter.lower().split(" ")
		if (cmd[0] + " " + cmd[1]) in bookList:
			entbook = cmd[0] + " " + cmd[1]
			withSub = True
		elif cmd[0] in bookList:
			entbook = cmd[0]
			withSub = False
		else:
			return False
	#test verset
		if not withSub:
			verset = cmd[1].split(":")[0]
			subverset = cmd[1].split(":")[1]#.split(",")
		else:
			verset = cmd[2].split(":")[0]
			subverset = cmd[2].split(":")[1]#.split(",")
	#activate
		self.book = entbook
		self.raw_verset = verset+":"+subverset
		self.verset1 = verset
		self.raw_verset2 = subverset
		self.verset2 = subverset
		
		