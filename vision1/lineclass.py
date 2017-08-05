
class Line :
	def __init__(self,line,line_list):
		self.line = line
		self.time = line_list[0]
		self.name = line_list[1]
		self.content = line_list[2]
		self.line_list = line_list
		self.word_list = []

	def return_name(self):
		return self.name
	
	def search_Target_Throughout(self,target_word):
		the_same = 1
		if(len(target_word) > len(self.content)):
			return 0

		for i in range(0,len(self.content)):
			for x in range(0,len(target_word)):

				if(i+x >= len(self.content)):
					return 0
				if(self.content[i+x] == target_word[x]):
					the_same = the_same * 1
				else:
					the_same = 0

			if(the_same == 1):
				return self.line
			the_same = 1

		return 0

	def search_Target_Solo(self,target_word):
		target_word = target_word +"\n"
		if(self.content == target_word):
			return self.line
		else:
			return 0

	def printListValue(self):
		print(self.time)
		print(self.name)
		print(self.content)

	def catchWordFromContent(self):
		for i in range(len(self.content) - 1):
			self.word_list.append(self.content[i] + self.content[i+1])

