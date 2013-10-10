import unittest
from simpleCredit.util import *

class UtilTest(unittest.TestCase) :

	def testLuhnChecksumValid(self):
		LuhnSN1 = '4111111111111111'
		LuhnSN2 = '5454545454545454'
		LuhnSN3 = '79927398713'
		
		self.assertTrue(is_luhn_valid(LuhnSN1))
		self.assertTrue(is_luhn_valid(LuhnSN2))
		self.assertTrue(is_luhn_valid(LuhnSN3))

	def testLuhnChecksumInvalid(self):
		LuhnSN1Bad = '1234567890123456'
		LuhnSN2Bad = '4444333322221110'
		LuhnSN3Bad = '4222222222222222'
	
		self.assertFalse(is_luhn_valid(LuhnSN1Bad))
		self.assertFalse(is_luhn_valid(LuhnSN2Bad))
		self.assertFalse(is_luhn_valid(LuhnSN3Bad))


		

def main():
	unittest.main()

if __name__ == '__main__':
	main()
