import unittest
import sys 
import os
sys.path.append(os.path.abspath("/media/joh0829nny/DATA/main/程式/程式/line聊天搜尋/vision2"))
from timeclass import Time
from search import *

class utDate(unittest.TestCase):
	def test_test(self):
		self.assertEqual(1,1)

	def test_addSpeakerList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test_list = ['湯忠禮','0歐87']
		self.assertEqual(test_list,test.addSpeakerList())

	def test_addDateList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['24:33','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test_list = ['2017/07/21(週五)']
		self.assertEqual(test.addDateList(),test_list)

	def test_addDateListToDic(self):
		class_line_list = []
		test = Time(class_line_list)
		test.date_list = ['2017/07/21(週五)','2017/07/22(週六)']
		self.assertEqual({'2017/07/21(週五)': {}, '2017/07/22(週六)': {}},test.addDateListToDic())

	def test_addSpeakerListToDic(self):
		class_line_list = []
		test = Time(class_line_list)
		test.date_list = ['2017/07/21(週五)','2017/07/22(週六)']
		test.speaker_list = ['湯忠禮','0歐87']
		test.addDateListToDic()
		test_dic = {'2017/07/21(週五)': {'0歐87': 0, '湯忠禮': 0}, '2017/07/22(週六)': {'0歐87': 0, '湯忠禮': 0}}
		self.assertEqual(test_dic,test.addSpeakerListToDic())

	def test_addSpeakerMessageCount(self):
		class_line_list = []
		test = Time(class_line_list)
		test.date_list = ['2017/07/21(週五)','2017/07/22(週六)']
		test.speaker_list = ['湯忠禮','0歐87']
		test.addDateListToDic()
		test.addSpeakerListToDic()
		test.date = '2017/07/21(週五)'
		test.speaker = '湯忠禮'
		test_dic = {'2017/07/21(週五)': {'0歐87': 0, '湯忠禮': 1}, '2017/07/22(週六)': {'0歐87': 0, '湯忠禮': 0}}
		self.assertEqual(test_dic,test.addSpeakerMessageCount())

	def test_differenceTime(self):
		class_line_list = []
		test = Time(class_line_list)
		time1_list = [20,30]
		time2_list = [21,20]
		test_list = [1,-10]
		differ_time_list = test.differenceTime(time1_list,time2_list)
		self.assertEqual(test_list,differ_time_list)

	def test_transformStringToTime(self):
		class_line_list = []
		test = Time(class_line_list)
		timestring = '23:59'
		self.assertEqual([23,59],test.transformStringToTime(timestring))

	def test_calculateDifferentTime(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['24:35','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test.classlinelist_index = 1
		self.assertEqual([0,2],test.calculateDifferentTime())

	def test_transformTimeListIntoTimeNumber(self):
		class_line_list = []
		test = Time(class_line_list)
		different_time_list = [5,20]
		self.assertEqual(320,test.transformTimeListIntoTimeNumber(different_time_list)) 	

	def test_transformTimeListIntoTimeNumber2(self):
		class_line_list = []
		test = Time(class_line_list)
		different_time_list = [5,-10]
		self.assertEqual(290,test.transformTimeListIntoTimeNumber(different_time_list)) 	

	def test_addReplyTimeInReplyList(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.speaker_match_reply_list = [[],[]]
		self.assertEqual([[130],[]],test.addReplyTimeInReplyList('湯忠禮',[2,10]))

	def test_determineReply(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['24:36','0歐87','啊要帶零食嗎\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.speaker_match_reply_list = [[],[]]
		test.classlinelist_index = 1
		self.assertEqual([[],[3]],test.determineReply())

	def test_createReplyList(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['24:36','0歐87','啊要帶零食嗎\n'],['24:54','湯忠禮','123\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.classlinelist_index = 1
		self.assertEqual([[18],[3]],test.createReplyList())

	def test_ccreateReplyList2(self):
		stringlist = [['2017/07/21(週五)\n'],['24:33','湯忠禮','我知道你是誰\n'],['1:10','0歐87','啊要帶零食嗎\n'],['1:20','湯忠禮','123\n']]
		class_line_list = throwListToClass(stringlist)
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.classlinelist_index = 1
		self.assertEqual([[10],[37]],test.createReplyList())

	def test_calculateReplyListAverage(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_match_reply_list = [[2,1,3,4]]
		self.assertEqual([2.5],test.calculateReplyListAverage())

	def test_calculateReplyListStd(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_match_reply_list = [[2,2,2,2]]
		self.assertEqual([0],test.calculateReplyListStd())


'''
	def test_addCountInDictionary(self):
		class_line_list = []
		test = Time(class_line_list)
		dictionary_big = {'big':{'1':5}}
		dictionary_big['big'] = test.addCountInDictionary(1,dictionary_big['big'])
		self.assertEqual({'big':{'1':6}},dictionary_big)

	def test_determineIfDicHasThisNumber(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.sumReplylist_Ditionary = {'湯忠禮':{},'0歐87':{}}
		self.assertEqual(0,test.determineIfDicHasThisNumber(0,1))

	def test_determineIfDicHasThisNumber2(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.sumReplylist_Ditionary = {'湯忠禮':{'1':5},'0歐87':{}}
		self.assertEqual(1,test.determineIfDicHasThisNumber(0,1))

	def test_forLoopSpeakerReplyList(self):
		class_line_list = []
		test = Time(class_line_list)
		test.speaker_list = ['湯忠禮','0歐87']
		test.sumReplylist_Ditionary = {'湯忠禮':{'1':5},'0歐87':{}}

'''
