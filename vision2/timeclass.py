
hour_index_ten = 0
hour_index_one = 1
minute_index_ten = 3
minute_index_one = 4

from classlinelist import LineList
import numpy as np

class Time(LineList):
	"""docstring for Time"""
	def __init__(self, class_line_list):
		#super(Time, self).__init__()
		self.date_list = []
		self.class_line_list = class_line_list
		self.date_message_list = []
		self.timeInclude_NameMatchMessage_dic = {}
		self.speaker_list = []
		self.speaker_match_reply_list = []
		self.average_reply_list = []
		self.std_reply_list = []

		self.classlinelist_index = 0
		self.date = ""
		self.speaker = ""


	def printAverageReplyList(self):
		print(self.average_reply_list)
	def printStdReplyList(self):
		print(self.std_reply_list)



	def number_Initailize(self):
		return 0


	def addSpeakerList(self):
		for i in range(len(self.class_line_list)):
			if(self.determineIfNotInList(self.class_line_list[i].name,self.speaker_list)):
				self.speaker_list.append(self.class_line_list[i].name)

		return self.speaker_list

	def addDateList(self):
		for i in range(len(self.class_line_list)):
			if(self.determineIfNotInList(self.class_line_list[i].date,self.date_list)):
				self.date_list.append(self.class_line_list[i].date)

		return self.date_list




	def prepareForDictionary(self):
		self.addDateListToDic()
		self.addSpeakerListToDic()
		return self.timeInclude_NameMatchMessage_dic
	
	def addDateListToDic(self):
		for date in (self.date_list):
			self.timeInclude_NameMatchMessage_dic[date] = {}
		return self.timeInclude_NameMatchMessage_dic

	def addSpeakerListToDic(self):
		for speaker in self.speaker_list:
			for date in (self.date_list):
				self.timeInclude_NameMatchMessage_dic[date][speaker] = 0
		return self.timeInclude_NameMatchMessage_dic




	def countEverydayMessage(self):
		count = 0
		for date in (self.date_list):
			for class_line in self.class_line_list:
				if(class_line.date == date):
					count = count + 1

			self.date_message_list.append(count)
			count = self.number_Initailize()

		return self.date_message_list


	def countEverydayEverybodyMessage(self):
		for self.date in (self.date_list):
			self.forLoopInClasslinelist()
		return self.timeInclude_NameMatchMessage_dic

	def forLoopInClasslinelist(self):
		for self.classlinelist_index in range(len(self.class_line_list)):
			self.determineDateEqual()
			
	def determineDateEqual(self):
		if(self.class_line_list[self.classlinelist_index].date == self.date):
			self.addSpeakerMessage()


	def addSpeakerMessage(self):
		for self.speaker in (self.speaker_list):
			self.determineSpeakerEqual()

	def determineSpeakerEqual(self):
		if(self.class_line_list[self.classlinelist_index].name == self.speaker):
			self.addSpeakerMessageCount()

	def addSpeakerMessageCount(self):
		count = self.timeInclude_NameMatchMessage_dic[self.date][self.speaker]
		count = count + 1
		self.timeInclude_NameMatchMessage_dic[self.date][self.speaker] = count

		return self.timeInclude_NameMatchMessage_dic






	def createReplyList(self):
		self.createReplyListSublistFromSpeakerNum()
		for self.classlinelist_index in range(1,len(self.class_line_list)):
			self.determineReply()
		return self.speaker_match_reply_list

	def createReplyListSublistFromSpeakerNum(self):
		for i in range(len(self.speaker_list)):
			self.speaker_match_reply_list.append([])
		return self.speaker_match_reply_list

	def determineReply(self):
		speaker_name = self.class_line_list[self.classlinelist_index - 1].name
		reply_name = self.class_line_list[self.classlinelist_index].name

		if(self.determineIfIsAnotherReply(reply_name,speaker_name)):
			different_time_list = self.calculateDifferentTime()
			self.speaker_match_reply_list = self.addReplyTimeInReplyList(reply_name,different_time_list)

		return self.speaker_match_reply_list

	def determineIfIsAnotherReply(self,reply_name,speaker_name):
		if(reply_name != speaker_name):
			return 1
		else:
			return 0

	def addReplyTimeInReplyList(self,reply_name,different_time_list):
		for speaker_list_index in range(len(self.speaker_list)):
			speaker_name = self.speaker_list[speaker_list_index]

			if(self.determineTheSameName(speaker_name,reply_name)):
				sum_minute = self.transformTimeListIntoTimeNumber(different_time_list)
				self.speaker_match_reply_list[speaker_list_index].append(sum_minute)

		return self.speaker_match_reply_list

	def transformTimeListIntoTimeNumber(self,different_time_list):
		hour = different_time_list[0]
		minute = different_time_list[1]
		sum_minute = hour * 60 + minute
		sum_minute = self.determineIfIsNegative(sum_minute)
		return sum_minute

	def determineIfIsNegative(self,sum_minute):
		if(sum_minute) < 0:
			sum_minute = sum_minute + 1440
		return sum_minute

	def determineTheSameName(self,speaker_name,reply_name):
		if(speaker_name == reply_name):
			return 1
		else:
			return 0

	def calculateDifferentTime(self):
		time1 = self.class_line_list[self.classlinelist_index - 1].time
		time2 = self.class_line_list[self.classlinelist_index].time
		time1_list = self.transformStringToTime(time1)
		time2_list = self.transformStringToTime(time2)
		different_time_list = self.differenceTime(time1_list,time2_list)
		return different_time_list

	def transformStringToTime(self,time_string):
		hour,minute = time_string.split(":")
		hour = int(hour)
		minute = int(minute)
		return [hour, minute]

	def differenceTime(self,time1_list,time2_list):
		different_time_list= [[],[]]
		for i in range(len(time1_list)):
			different_time_list[i] = time2_list[i] - time1_list[i]
		return different_time_list		




	def calculateReplyList(self):
		self.calculateReplyListAverage()
		self.calculateReplyListStd()

	def calculateReplyListAverage(self):
		for i in range(len(self.speaker_match_reply_list)):
			self.average_reply_list.append(np.average(self.speaker_match_reply_list[i]))
		return (self.average_reply_list)

	def calculateReplyListStd(self):
		for i in range(len(self.speaker_match_reply_list)):
			self.std_reply_list.append(np.std(self.speaker_match_reply_list[i]))
		return (self.std_reply_list)




'''

	def SumReplyListInDictioanry(self):
		self.addSpeakerlistInDictionary()
		for speaker_list_index in range(len(self.speaker_match_reply_list)):
			self.forLoopInSpeakerReplyList(speaker_list_index)

	def addSpeakerlistInDictionary(self):
		for speaker in self.speaker_list:
			self.sumReplylist_Ditionary[speaker] = {}
		return self.sumReplylist_Ditionary

	def forLoopSpeakerReplyList(self,speaker_list_index):
		for replylist_index in range(len(self.speaker_match_reply_list[speaker_list_index])):

			reply_value = self.speaker_match_reply_list[speaker_list_index][replylist_index]
			
			if(self.determineIfDicHasThisNumber(speaker_list_index,reply_value)):
				self.sumReplylist_Ditionary[speaker_list_index] = self.addCountInDictionary(reply_value,self.sumReplylist_Ditionary[speaker_list_index])
			else:
				self.sumReplylist_Ditionary[speaker_list_index][reply_value] = 1 

	def determineIfDicHasThisNumber(self,speaker_list_index,reply_value):
		speaker_name = self.speaker_list[speaker_list_index]
		if(str(reply_value) in self.sumReplylist_Ditionary[speaker_name].keys()):
			return 1
		else:
			return 0

	def addCountInDictionary(self,value,dictionary):
		count = dictionary[str(value)]
		count = count + 1
		dictionary[str(value)] = count
		return dictionary

'''