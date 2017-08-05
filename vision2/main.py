import sys 
import os
sys.path.append(os.path.abspath("/media/joh0829nny/DATA/main/程式/程式/line聊天搜尋/vision2/search"))
from search import *
from classlinelist import LineList
from timeclass import Time

content_lines = []
split_lines = []
class_line_list =[]
speaker_list = []
all_word_list = []
name_contentMatchcount_dictionary = {}

content_lines = readFileGetLines()
#print(content_lines)

split_lines = linesSplit(content_lines)
#print(split_lines)

class_line_list = throwListToClass(split_lines)

linelist_class = LineList(class_line_list)
#linelist_class.printClassLineList()
linelist_class.forLoopSearchTarget("幹嘛")


linelist_class.addSpeakerList()
linelist_class.addSpeakerListToDic()
linelist_class.addNameMatchAllWordListTogether(2)
#linelist_class.print_name_ContentMatchCount_dictionary()


linelist_class.findHotWordCountRank()
linelist_class.findHotWordRank(0,30)

time_class = Time(class_line_list)
print(time_class.addDateList())
print(time_class.countEverydayMessage())
time_class.countEverydayEverybodyMessage()
time_class.addSpeakerList()
time_class.prepareForDictionary()
print(time_class.countEverydayEverybodyMessage())
time_class.createReplyList()
time_class.calculateReplyList()
time_class.printAverageReplyList()
time_class.printStdReplyList()


'''
for i in range(len(class_line_list)):
	print((class_line_list[i].date))
'''
'''
forLoopSearchTarget(class_line_list,"幹嘛")

speaker_list = addSpeakerList(class_line_list)
'''


