
class Line:
	"""docstring for line"""
	def __init__(self,date,split_line_list):
		super(Line, self).__init__()
		self.line = " "
		self.date = date
		self.time = split_line_list[0]
		self.name = split_line_list[1]
		self.content = split_line_list[2]
		self.split_line_list = split_line_list
		self.word_list = []

	def splitWordsInList(self,count):
		word = ""

		if(self.determineIfContentAddChangeLine()):
			content = self.content + "\n"
		else:
			content = self.content

		for i in range(len(content) - count + 1):
			for x in range(count):
				word = word + content[i + x ]
			self.word_list.append(word)
			word = ""
		return self.word_list

	def determineIfContentAddChangeLine(self,determine_number = 0):
		if(determine_number == 1):
			return 1
		else:
			return 0