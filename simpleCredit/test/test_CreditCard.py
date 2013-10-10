import unittest
from simpleCredit.CreditCard import *

class CreditCardTest(unittest.TestCase) :
	""" Test Class for CreditCard object """

	""" Test for new Card """
	def testCardCreate(self):
		expectedName = 'Tom'
		expectedSN   = '4111111111111111'
		expectedLimit = 1000
		expectedValidity = True
		
		testCard = CreditCard(expectedName,expectedSN,expectedLimit)
		self.assertEqual(testCard.getName(), expectedName)
		self.assertEqual(testCard.getSN(), expectedSN)
		self.assertEqual(testCard.getLimit() , expectedLimit)
		self.assertEqual(testCard.getBalance() , 0)
		self.assertEqual(testCard.isValid(), expectedValidity)
		

	def testCardCreate2(self):
		expectedName = 'Quincy'
		expectedSN   = '1234567890123456'
		expectedLimit = 2000
		expectedValidity = False
		
		testCard = CreditCard(expectedName,expectedSN,expectedLimit)
		self.assertEqual(testCard.getName() , expectedName)
		self.assertEqual(testCard.getSN(), expectedSN)
		self.assertEqual(testCard.getLimit() , expectedLimit)
		self.assertEqual(testCard.getBalance() , 0)
		self.assertEqual(testCard.isValid() , expectedValidity)

	"""testing the charge method"""
	def testChargeUnderLimit(self):
		Name = 'Tom'
		SN   = '4111111111111111'
		Limit = 1000
		
		testCard = CreditCard(Name,SN,Limit)
		amount = 500
		testCard.charge(amount)
		self.assertEqual(testCard.getBalance(),500)	

	def testChargeExceedLimit(self):
		Name = 'Tom'
		SN   = '4111111111111111'
		Limit = 1000
		
		testCard = CreditCard(Name,SN,Limit)
		amount = 500
		testCard.charge(amount)
		self.assertEqual(testCard.getBalance(),500)	
		testCard.charge(1000)
		self.assertEqual(testCard.getBalance(),500)
	
	def testChargeToInvalidCard(self):
		Name = 'Quincy'
		SN   = '1234567890123456'
		Limit = 2000
	
		testCard = CreditCard(Name,SN,Limit)
		amount =1000
		testCard.charge(amount)
		self.assertEqual(testCard.getBalance(),0)		


	"""Testing the Credit operation"""

	def testCreditToValidCard(self):	
		Name = 'Tom'
		SN   = '4111111111111111'
		Limit = 1000
		
		testCard = CreditCard(Name,SN,Limit)
		amount = 500
		testCard.charge(amount)
		self.assertEqual(testCard.getBalance(),500)	
		
		"""test credit < current balance"""	
	
		credit_amount = 200
		testCard.credit(credit_amount)

		self.assertEqual(testCard.getBalance(),300)
		
		"""test Credit > current balance"""
		
		credit_amount = 400
		testCard.credit(credit_amount)
		self.assertEqual(testCard.getBalance(),-100)	
	
	def testCreditToInvalidCard(self):
		Name = 'Quincy'
		SN   = '1234567890123456'	
		Limit = 1000
		
		testCard = CreditCard(Name,SN,Limit)
		credit_amount = 400
		testCard.credit(credit_amount)
		self.assertEqual(testCard.getBalance(),0)	
	
def main():
	unittest.main()

if __name__ == '__main__':
	main()
