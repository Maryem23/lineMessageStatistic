
class LineList(object):
	"""docstring for LineList"""
	def __init__(self,class_line_list):
		super(LineList, self).__init__()
		self.class_line_list = class_line_list
		self.speaker_list = []
		self.all_word_list = []
		self.date_list = []
		self.name_ContentMatchCount_dictionary = {}

		self.classlinelist_index = 0
		self.word_list_index = 0
		self.word_list = []
		self.speaker_name = " "
		self.speakerlist_index = 0
		self.count_in_dic_list = []
		self.sorted_count_in_dic_list = []
		self.all_sorted_count_in_dic_list = []
		self.word = " "
		self.count = 0
		self.sort_list_index = 0
		self.all_sorted_list_index = 0
		self.date_message_list = []

	def printClassLineList(self):
		print(self.class_line_list)

	def print_name_ContentMatchCount_dictionary(self):
		print(self.name_ContentMatchCount_dictionary)

	def forLoopSearchTarget(self,TargetString):
		count = 0

		for i in range(len(self.class_line_list)):
			if(self.haveSearchTarget(i,TargetString)):
		 		count = count + 1
		 		self.printWholeLineInformation(i,count)


	def printWholeLineInformation(self,classlinelist_index,count):
		class_line = self.class_line_list[classlinelist_index]
		print(str(count)+ ". " + class_line.date + class_line.time +"  "+class_line.name +"  "+ class_line.content)


	def haveSearchTarget(self,classlinelistindex,TargetString):
		content = self.class_line_list[classlinelistindex].content +"\n"
		the_same = 1
		if(self.determineIfContentLongerThanTargetstring(content,TargetString)):	

			for i in range(0,len(content)):
				for x in range(0,len(TargetString)):

					if(self.determineIndexOutOfRange(i+x,len(content))):
						return 0

					if(self.determineCharOfContentEqualTargetstring(content[i+x],TargetString[x])):
						the_same = the_same * 1
					else:
						the_same = 0

				if(the_same == 1):
					return 1
				the_same = 1

			return 0
		
		else:
			return 0

	def determineIfContentLongerThanTargetstring(self,content,TargetString):
		if(len(content) > len(TargetString)):
			return 1
		else:
			return 0

	def determineIndexOutOfRange(self,index,contentlength):
		if(index >= contentlength):
			return 1
		else:
			return 0

	def determineCharOfContentEqualTargetstring(self,contentchar,TargetStringchar):
		if(contentchar == TargetStringchar):
			return 1 
		else:
			return 0



	def addSpeakerList(self):
		for i in range(len(self.class_line_list)):
			if(self.determineIfNotInList(self.class_line_list[i].name,self.speaker_list)):
				self.speaker_list.append(self.class_line_list[i].name)
		return self.speaker_list

	def determineIfNotInList(self,element,list):
		if(element not in list):
			return 1
		else:
			return 0
			

	def addSpeakerListToDic(self):
		for i in range(len(self.speaker_list)):
			self.name_ContentMatchCount_dictionary[self.speaker_list[i]] = {}
		return self.name_ContentMatchCount_dictionary





	def addNameMatchAllWordListTogether(self,find_word_count):
		for self.classlinelist_index in range(len(self.class_line_list)):
			self.name_ContentMatchCount_dictionary = self.addWordListInDictionary(find_word_count)
		return self.name_ContentMatchCount_dictionary

	def addWordListInDictionary(self,find_word_count):
		self.word_list = self.class_line_list[self.classlinelist_index].splitWordsInList(find_word_count)
		#name_match_list = self.name_ContentMatchCount_dictionary[class_line.name]
		for self.word_list_index in range(len(self.word_list)):
			 self.name_ContentMatchCount_dictionary = self.addWordInDic()
		return self.name_ContentMatchCount_dictionary

	def addWordInDic(self):
		self.speaker_name = self.class_line_list[self.classlinelist_index].name
		self.word = self.word_list[self.word_list_index] 

		if(self.word in self.name_ContentMatchCount_dictionary[self.speaker_name].keys()):
			self.addWordCountInDic()
		else:
			self.name_ContentMatchCount_dictionary[self.speaker_name][self.word] = 1
		return self.name_ContentMatchCount_dictionary

	def addWordCountInDic(self):
		word_count = self.name_ContentMatchCount_dictionary[self.speaker_name][self.word]			
		word_count = word_count + 1
		self.name_ContentMatchCount_dictionary[self.speaker_name][self.word] = word_count
		return self.name_ContentMatchCount_dictionary





	def findHotWordRank(self,range_min,range_max):
		#print(self.findHotWordCountRank())
		for self.all_sorted_list_index in range(len(self.all_sorted_count_in_dic_list)):
			self.printSpeakerName()
			self.forLoopForSortCountList(range_min,range_max)

	def printSpeakerName(self):
		print("--------------------------------------")
		print(self.speaker_list[self.all_sorted_list_index] + "*************************")
		
				
	def forLoopForSortCountList(self,range_min,range_max):
		i = self.all_sorted_list_index
		for self.sort_list_index in range(range_min,range_max):
			if(self.determineRepeatRank()):
				pass
			else:
				self.forLoopForDictionary()

	def determineRepeatRank(self):
		i = self.all_sorted_list_index
		if(self.all_sorted_count_in_dic_list[i][self.sort_list_index] == self.all_sorted_count_in_dic_list[i][self.sort_list_index-1]):
			return 1
		else:
			return 0

	def forLoopForDictionary(self):
		i = self.all_sorted_list_index
		for self.word,self.count in self.name_ContentMatchCount_dictionary[self.speaker_list[i]].items():
			self.useCountCatchWord()


	def useCountCatchWord(self):
		i = self.all_sorted_list_index
		if(self.count == self.all_sorted_count_in_dic_list[i][self.sort_list_index]):
			print("                  "+str(self.sort_list_index + 1)+"."+str(self.word) + "  " + str(self.count))











	def findHotWordCountRank(self):
		for self.speakerlist_index in range(len(self.speaker_list)):	
			self.add_CountInDic_InList()
			self.sortCountList()

			self.count_in_dic_list = []
			self.all_sorted_count_in_dic_list.append(self.sorted_count_in_dic_list)
		return(self.all_sorted_count_in_dic_list)

	def add_CountInDic_InList(self):
		for word,count in self.name_ContentMatchCount_dictionary[self.speaker_list[self.speakerlist_index]].items():
			self.count_in_dic_list.append(count)
		return self.count_in_dic_list

	def sortCountList(self):		
		self.sorted_count_in_dic_list = sorted(self.count_in_dic_list,reverse = True)
		return self.sorted_count_in_dic_list







	def addDateList(self):
		for i in range(len(self.class_line_list)):
			if(self.determineIfNotInList(self.class_line_list[i].date,self.date_list)):
				self.date_list.append(self.class_line_list[i].date)
		return self.date_list

	def countEverydayMessage(self):
		count = 0
		for date in (self.date_list):
			for i in range(len(self.class_line_list)):
				if(self.class_line_list[i].date == date):
					count = count + 1
			self.date_message_list.append(count)
			count = self.number_Initailize()
		return self.date_message_list
	def number_Initailize(self):
		return 0


				