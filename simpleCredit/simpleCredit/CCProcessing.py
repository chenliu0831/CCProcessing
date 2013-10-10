import re
import sys
import operator

from operator import attrgetter,itemgetter
from simpleCredit.CreditCard import *
from simpleCredit.util import *

""" General Credit Card Processing and Summay"""


class CCProcessing:

	def __init__(self, infileName):
		self.__infileName = infileName
		
		self.__Object_Buffer = []

	def readAndProcessData(self):
		#parse input using space delimiter	
		separator = ' '
		for data in import_data(self.__infileName,separator):
			#Get the command, should be the first word
			Command = data[0]

			if Command == 'Add': 
				assert len(data) == 4
				self.setupNewCard(data)
			elif Command == 'Charge':
				assert len(data) == 3
				self.cardCharging(data)
			elif Command == 'Credit':
				assert len(data) == 3
				self.cardCrediting(data)
			else:
				#unknown command
				return False	
		
		return True

	def setupNewCard(self, data):
		CardName = data[1]
		CardSN   = data[2]
		CardLimit_str = data[3]
		CardLimit = int( re.sub("[^\d]","",CardLimit_str))
		
		newCard = CreditCard(CardName,CardSN,CardLimit)	
		self.__Object_Buffer.append(newCard)

	def cardCharging(self, data):
		CardName = data[1]
		Amount_str   = data[2]
		#remove leading $s using regex
		amount = int( re.sub("[^\d]","",Amount_str))
		#print(amount)
		
		#Get Existing Credit Card Object
		targetCard = self.__getObjectByName(CardName)
		targetCard.charge(amount)
	
	def cardCrediting(self,data):
		CardName = data[1]
		Amount_str   = data[2]
		#remove leading $s using regex
		amount = int( re.sub("[^\d]","",Amount_str))
		#print(amount)
		
		#Get Existing Credit Card Object
		targetCard = self.__getObjectByName(CardName)
		targetCard.credit(amount)
	
	#Summary to stdout
	def CCSummary(self):
		#sort first according to the Name
		
		self.__Object_Buffer.sort(key=operator.attrgetter("cardHolderName"))
		
		for card in self.__Object_Buffer:
			sys.stdout.write(card.getName())
			sys.stdout.write(':')
			if card.isValid():
				sys.stdout.write('$')
				sys.stdout.write(str(card.getBalance()))
			else:
				sys.stdout.write('error')
			print

		return True
	
	def __getObjectByName(self,Name):
		#Get Object by Name, using list comprehension
		#Should not return null or mutiple object list by assumption 
		_objlist = [obj for obj in self.__Object_Buffer if obj.getName()== Name]
		return _objlist[0]


	
	##for test use
	def getFirstObject(self):
		return self.__Object_Buffer[0]	
