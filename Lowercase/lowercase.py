# Solution for codeeval lowercase problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '27-Feb-2015'

import sys

class Lowercase():

	""" Solution for codeeval lowercase problem  """

	def __init__(self,filename):

		""" Initial function in Lowercase class """

		self.filename = filename

	def readfile(self):

		""" Reads the input file """

		with open(self.filename,'r') as f:
			for line in f:
				print line.lower()

def main():

	""" Main function create Lowercase instance and get use of it """

	filename = sys.argv[1]
	lowercase = Lowercase(filename)
	lowercase.readfile()

if __name__ == "__main__":
	main()