# Solution for codeeval calculate distance problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '07-Mar-2015'

import sys
from math import sqrt

class CalculateDistance():

	""" Solution for codeeval calculate distance problem """

	def __init__(self,filename):

		""" Initial function i CalculateDistance class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file by line by line """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.get_result(line)

	def get_result(self, line):

		""" splits the line to four integers and find the distance """

		self.line = line
		splited_string = self.line.split()
		numbers_list = [int(x.translate(None,')(,')) for x in splited_string]
		return int(sqrt( (numbers_list[2] - numbers_list[0])**2 + (numbers_list[3] - numbers_list[1])**2 ))

def main():

	""" main function to create CalculateDistance class instance and get use of it """

	filename = sys.argv[1]
	calculatedistance = CalculateDistance(filename)
	calculatedistance.read_file()

if __name__ == "__main__":
	main()
