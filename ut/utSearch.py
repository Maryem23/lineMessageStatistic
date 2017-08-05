import unittest
import sys 
import os
sys.path.append(os.path.abspath("/media/joh0829nny/DATA/main/程式/程式/line聊天搜尋/vision2"))
from search import *

class utSearch(unittest.TestCase):
	def test_test(self):
		self.assertEqual(1,1)

	def test_lineSplit(self):
		stringlist = ['24:33\t湯忠禮\t嗯嗯\n', '24:33\t0歐87\t啊要帶零食嗎\n']
		split_string = linesSplit(stringlist)
		self.assertEqual(split_string,[['24:33','湯忠禮','嗯嗯\n'],['24:33','0歐87','啊要帶零食嗎\n']])

	def test_lineSplit2(self):
		stringlist =  ['2017/07/21(週五)\n']
		split_string = linesSplit(stringlist)
		self.assertEqual(split_string,[['2017/07/21(週五)\n']])

	def test_determineIfDate(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯\n']]
		self.assertEqual(1,determineIfDate(stringlist[0]))
		self.assertEqual(0,determineIfDate(stringlist[1]))

	def test_throwlistToClass(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯\n']]
		class_line_list = throwListToClass(stringlist)
		self.assertEqual(class_line_list[0].date,'2017/07/21(週五)')
		self.assertEqual(class_line_list[0].time,'24:33')
		self.assertEqual(class_line_list[0].name,'湯忠禮')
		self.assertEqual(class_line_list[0].content,'嗯嗯')

	def test_deleteChangeLineSymbol(self):
		stringlist = '2017/07/21(週五)\n'
		self.assertEqual(deleteChangeLineSymbol(stringlist),'2017/07/21(週五)')

	def test_Class_Linelist_determineIfContentLongerThanTargetstring(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		self.assertEqual(1,test.determineIfContentLongerThanTargetstring(test.class_line_list[0].content,"嗯"))

	def test_Class_Linelist_determineIndexOutOfRange(self):
		class_line_list = []
		test = LineList(class_line_list)
		index = 10
		contentlength = 8
		self.assertEqual(1,test.determineIndexOutOfRange(index,contentlength))
	
	def test_Class_Linelist_determineCharOfContentEqualTargetstring(self):
		class_line_list = []
		test = LineList(class_line_list)
		contentchar = '道'
		TargetStringchar = '道'
		self.assertEqual(1,test.determineCharOfContentEqualTargetstring(contentchar,TargetStringchar))


	def test_haveSearchTarget(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		TargetString = "你是"
		self.assertEqual(1,test.haveSearchTarget(0,TargetString))

	def test_haveSearchTarget2(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		TargetString = "我知"
		self.assertEqual(1,test.haveSearchTarget(0,TargetString))

	def test_searchTarget3(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		TargetString = "你誰"
		self.assertEqual(0,test.haveSearchTarget(0,TargetString))

	def test_searchTarget4(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		TargetString = "我知道你是誰"
		self.assertEqual(0,test.haveSearchTarget(0,TargetString))

	def test_Line_spiltWordsInList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n']]
		determinestringlist =['嗯嗯','嗯我']
		class_line_list = throwListToClass(stringlist)
		self.assertEqual(class_line_list[0].date,'2017/07/21(週五)')
		self.assertEqual(class_line_list[0].time,'24:33')
		self.assertEqual(class_line_list[0].name,'湯忠禮')
		self.assertEqual(class_line_list[0].content,'嗯嗯我')
		self.assertEqual(class_line_list[0].splitWordsInList(2),determinestringlist)

	def test_addSpeakerList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		speaker_list = ['湯忠禮','0歐87']
		self.assertEqual(speaker_list,test.addSpeakerList())

	def test_addSpeakerListToDic(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		speaker_list = ['湯忠禮','0歐87']
		test_dictionary = {'湯忠禮':{},'0歐87':{}}
		self.assertEqual(speaker_list,test.addSpeakerList())
		self.assertEqual(test_dictionary,test.addSpeakerListToDic())

	def test_addWordCountInDic(self):
		class_line_list = []
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{'嗯嗯':1}}
		test.speaker_name = '湯忠禮'
		test.word = '嗯嗯'
		self.assertEqual({'湯忠禮':{'嗯嗯':2}},test.addWordCountInDic())

	def test_addWordInDic(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{}}
		test.classlinelist_index = 0
		test.word_list_index = 0
		test.word_list = ['嗯嗯']
		self.assertEqual({'湯忠禮':{'嗯嗯':1}},test.addWordInDic())

	def test_addWordInDic2(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{'嗯嗯':1}}
		test.classlinelist_index = 0
		test.word_list_index = 0
		test.word_list = ['嗯嗯']
		self.assertEqual({'湯忠禮':{'嗯嗯':2}},test.addWordInDic())

	def test_addWordListInDictionary(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{},'0歐87':{}}
		test.classlinelist_index = 0
		self.assertEqual({'湯忠禮': { '嗯嗯': 1, '嗯我': 1},'0歐87':{}},test.addWordListInDictionary(2))
		test.classlinelist_index = 1
		self.assertEqual({'0歐87': {'要帶': 1, '零食': 1, '食嗎': 1, '帶零': 1, '啊要': 1}, '湯忠禮': {'嗯我': 1, '嗯嗯': 1}}
,test.addWordListInDictionary(2))

	def test_addNameMatchAllWordListTogether(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{},'0歐87':{}}
		self.assertEqual({'0歐87': {'要帶': 1, '零食': 1, '食嗎': 1, '帶零': 1, '啊要': 1}, '湯忠禮': {'嗯我': 1, '嗯嗯': 1}}
,test.addNameMatchAllWordListTogether(2))

	def test_sortCountList(self):
		class_line_list = []
		test = LineList(class_line_list)
		test.count_in_dic_list = [5,2,4,7,8]
		self.assertEqual([8,7,5,4,2],test.sortCountList())

	def test_add_CountInDic_InList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯我\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{},'0歐87':{}}
		test.addNameMatchAllWordListTogether(2)
		test.speaker_list = ['湯忠禮','0歐87']
		test.speakerlist_index = 0
		self.assertEqual([1, 1],test.add_CountInDic_InList())
	
	def test_findHotWordCountRank(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯嗯嗯我\n'],['24:33','0歐87','啊要帶零帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{},'0歐87':{}}
		test.addNameMatchAllWordListTogether(2)
		test.speaker_list = ['湯忠禮','0歐87']
		test_list = [[3, 1],[2, 1, 1, 1, 1, 1]]
		self.assertEqual(test_list,test.findHotWordCountRank())

	def test_findHotWordRank(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','嗯嗯嗯嗯我\n'],['24:33','0歐87','啊要帶零帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = LineList(class_line_list)
		test.name_ContentMatchCount_dictionary = {'湯忠禮':{},'0歐87':{}}
		test.addNameMatchAllWordListTogether(2)
		test.speaker_list = ['湯忠禮','0歐87']
		test.findHotWordRank(0,30)







