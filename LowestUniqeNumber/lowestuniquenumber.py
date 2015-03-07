# Solution for codeeval lowest unique number problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '07-Mar-2015'

import sys

class LowestUniqueNumber():

	""" Solution for codeeval lowest unique number problem """

	def __init__(self,filename):

		""" Initial function in LowestUniqueNumber class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and generates inputs """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.uniquenumber(line)

	def uniquenumber(self, line):

		""" find the lowest unique number """

		self.line = line.replace("\n", "")
		number_list = [int(x) for x in self.line.split()]
		uniquenumbers = [x for x in number_list if number_list.count(x) == 1]
		if uniquenumbers:
			uniquenumbers.sort()
			return number_list.index(uniquenumbers[0]) + 1
		else:
			return 0

def main():

	""" main function to create LowestUniqueNumber instance and get use of it """

	filename = sys.argv[1]
	lowestuniquenumber = LowestUniqueNumber(filename)
	lowestuniquenumber.read_file()

if __name__ == "__main__":
	main()