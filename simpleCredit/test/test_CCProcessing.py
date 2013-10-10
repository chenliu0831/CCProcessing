import unittest
from simpleCredit.CreditCard import *
from simpleCredit.util       import *
from simpleCredit.CCProcessing import *

"""CreditCard Processing Module Test"""

class CCProcessingTest(unittest.TestCase) :

	def testReadProcessData(self):
	       inputFileName = 'input.txt'
	       

	       testCCP =CCProcessing(inputFileName)
	       self.assertTrue(testCCP.readAndProcessData())

	       #dirty..use the first in list
	       sampleCC = testCCP.getFirstObject()
	       
	       self.assertEqual(sampleCC.getBalance(),500) 	
		
	       self.assertTrue(testCCP.CCSummary())

	def testReadProcessData2(self):
		inputFileName = 'input2.txt'
		testCCP =CCProcessing(inputFileName)
	        self.assertTrue(testCCP.readAndProcessData())

	        sampleCC = testCCP.getFirstObject()
	       
	        self.assertEqual(sampleCC.getBalance(),-100) 	
		
	        self.assertTrue(testCCP.CCSummary())

	
def main():
	unittest.main()

if __name__ == '__main__':
	main()

