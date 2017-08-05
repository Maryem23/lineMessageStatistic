from classline import Line
from classlinelist import LineList


def readFileGetLines():
	file = open('87ou.txt')
	lines = file.readlines()
	return(lines)

def linesSplit(lines):
	split_line_list = []
	for line in lines:
		split_lines = line.split("\t")
		split_line_list.append(split_lines)
	return(split_line_list)	

def throwListToClass(split_line_list):
	class_line_list = []
	for i in range(len(split_line_list)):
		
		if(determineIfDate(split_line_list[i])):
			 date = deleteChangeLineSymbol(split_line_list[i][0])
		
		else:
			split_line_list[i][2] = deleteChangeLineSymbol(split_line_list[i][2])
			
			class_line = Line(date,split_line_list[i])
			class_line_list.append(class_line)

	return class_line_list

def determineIfDate(stringlist):
	if(len(stringlist) == 1):
		return 1
	else:
		return 0		

def deleteChangeLineSymbol(string):
	if(string[len(string)-1] == '\n'):
		string_new,changeline = string.split("\n")
	return(string_new)








'''
def addNameMatchAllWordListTogether(class_line_list,speaker_list,name_ContentMatchCount_dictionary):
	for i in range(len(class_line_list)):
		word_list = class_line_list[i].splitWordsInList(2)
		name_ContentMatchCount_dictionary = addWordListInDictionary(class_line_list[i],word_list,name_ContentMatchCount_dictionary)

'''
'''
def addWordListInDictionary(class_line,word_list,dictionary):
	name_match_list = dictionary[class_line.name]
	for i in range(len(word_list)):
		countWordInDic(word_list[i],dictionary[class_line.name])

def countWordInDic(word,wordMatchCountDictionary):
	#if(word in wordMatchCountDictionary.keys()):
		#addWordCountValue(word,)


'''


'''
def throwClassListInDictionary(class_line_list,name_contentMatchcount_dictionary):
	for i in range(len(class_line_list)):
		word_list = class_line_list[i].splitWordsInList(2)
		addNameMatchWordListInDictionary(class_line_list[i].name,word_list,name_contentMatchcount_dictionary)

def addNameMatchWordListInDictionary(speakerName,word_list,name_contentMatchcount_dictionary):
	name_contentMatchcount_dictionary[speakerName] = word_list
'''