file = open('87ou.txt')
blank = " "
from lineclass import Line

def split_Lines(line):
	string_list = []
	string_list = line.split(" ")
	return(string_list)

def stringlistToLinelist(string_list):
	line_list = string_list[0].split("\t")
	return(line_list)

def determineIsChatContent(line_list):
	if(len(line_list))==3:
		return 1
	else:
		return 0

def determineStringlistNumber(string_list):
	if(len(string_list) >= 2):
		return 1
	else:
		return 0

def addLinelist(stringlistLength,line_list):
	for i in range(1,stringlistLength):
		line_list[2] = line_list[2] + string_list[i]
	return line_list

def calculateTargetFromUser(name,calculateTargetDictionary):
	if(str(name) in calculateTargetDictionary):
		target_count = calculateTargetDictionary[str(name)]
		target_count = target_count + 1
		calculateTargetDictionary[str(name)] = target_count
	else:
		calculateTargetDictionary[str(name)] = 1

	return calculateTargetDictionary

def addSpeakerList(name,speaker_list):
	if (name in speaker_list):
		pass
	else:
		speaker_list.append(name)

def addSpeakerToWordDictionary(speaker_list,wordDictionary):
	for i in range(len(speaker_list)):
		if(speaker_list[i] not in wordDictionary):
			key = speaker_list[i]
			wordDictionary[key] = {}

def addWordlistInDictionary(name,word_list,wordDictionary):
	for i in range(len(word_list)):
		calculateTargetFromUser(word_list[i],wordDictionary[name])
	#print(wordDictionary)
	#return wordDictionary
def getNameMatchSortedCountListDic(wordDictionary):
	count_list = []
	nameMatchCountSortedListDic = {}

	for speaker_name in wordDictionary.keys():
		for word,count in wordDictionary[speaker_name].items():
			count_list.append(count)
			sort_count_list = sorted(count_list,reverse = True)

		nameMatchCountSortedListDic[speaker_name] = sort_count_list
		count_list = []
		sort_count_list = []
	return(nameMatchCountSortedListDic)
	#print(list(wordDictionary[speaker_list[0]].keys())[list(wordDictionary[speaker_list[0]].values()).index(16)])

def searchHotWord(allNameMatchSortedCountListDic,wordDictionary):
	rank_min = 0
	rank_max = 40
	for speaker_name in allNameMatchSortedCountListDic.keys():
		print(speaker_name + "***********************")
		for i in range(rank_min,rank_max):

			if(determine_count_repeat(allNameMatchSortedCountListDic[speaker_name],i)):

				for word,count in wordDictionary[speaker_name].items():
					
					if(count == allNameMatchSortedCountListDic[speaker_name][i]):

								print(str(word) + "--->" + str(count))
			else:
				pass
			
		print("--------------------------------------")

def determine_count_repeat(sort_rank_list,rank_now):
	if(rank_now >= 1):
		if(sort_rank_list[rank_now] != sort_rank_list[rank_now - 1]):
			return 1
		else:
			return 0
	else:
		return 1


lines = file.readlines()
includeTargetStringList = []
string_list = []
line_list = []
classLineList = []
word_list = []
speaker_list = []
wordDictionary = {}
calculateTargetDictionary = {}
allNameMatchSortedCountListDic = {}


count = 0
lines.remove('\ufeff[LINE] 與0歐87的聊天記錄\n')
lines.remove('儲存日期：2017/07/29 15:59\n')

for line in lines:
	string_list = split_Lines(line)
	line_list = stringlistToLinelist(string_list)

	if(determineIsChatContent(line_list)):
		if(determineStringlistNumber(string_list)):
			line_list = addLinelist(len(string_list),line_list)


		class_line = Line(line,line_list)
		classLineList.append(Line(line,line_list))

		addSpeakerList(class_line.name,speaker_list)
		addSpeakerToWordDictionary(speaker_list,wordDictionary)
		


		if(class_line.search_Target_Throughout("幹嘛")):
			count = count + 1
			calculateTargetDictionary = calculateTargetFromUser(class_line.name,calculateTargetDictionary)
			class_line.printListValue()
			#print(calculateTargetDictionary)
		
		class_line.catchWordFromContent()
		addWordlistInDictionary(class_line.name,class_line.word_list,wordDictionary)

allNameMatchSortedCountListDic = getNameMatchSortedCountListDic(wordDictionary)
searchHotWord(allNameMatchSortedCountListDic,wordDictionary)
#print(allNameMatchSortedCountListDic)



			

#print(classLineList)	
#rint(type(line))
#print(type(lines))
#print(count)
#print(speaker_list)
#print(wordDictionary)
#print(wordDictionary.items())
