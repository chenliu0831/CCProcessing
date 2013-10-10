from simpleCredit.util import *

class CreditCard:

	"""CreditCard Object"""

	"""Constructor"""
	def __init__(self,cardHolderName,cardSN,cardLimit):
		self.cardHolderName = cardHolderName
		self.__SN           = cardSN
		self.__limit        = cardLimit
		self.__balance      = 0
		self.__validity     = True if is_luhn_valid(cardSN) else False 
	
	def getName(self):
		return self.cardHolderName
	
	def getSN(self):
		return self.__SN

	def getLimit(self):
		return self.__limit
	
	def isValid(self):
		return self.__validity
	
	def getBalance(self):
		return self.__balance

	def charge(self,amount): 
		if self.isValid():
			subtotal = self.__balance + amount
			if subtotal <= self.__limit:
				self.__balance += amount

		
	def credit(self, amount):
		if self.isValid():
			self.__balance -=amount
