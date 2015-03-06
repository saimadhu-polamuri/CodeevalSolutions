# Solution for codeeval swap case problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '04-Mar-2015'

import sys

class Swapcase():

	""" Solution for codeeval swap case problem  """

	def __init__(self,filename):

		""" Initial function in Swapcase class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and genrates the swap case result """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.swapchange(line)

	def swapchange(self,line):

		""" Swap each character  upper to lower and vise verse """

		self.line = line
		given_line = ''
		for i in xrange(0,len(self.line)):
			if self.line[i].islower():
				given_line = given_line+ self.line[i].upper()
			else:
				given_line = given_line+ self.line[i].lower()

		return given_line



def main():

	""" main function to create Swapcase instance and get use of it """

	filename = sys.argv[1]
	swapcase = Swapcase(filename)
	swapcase.read_file()

if __name__ == "__main__":
	main()
