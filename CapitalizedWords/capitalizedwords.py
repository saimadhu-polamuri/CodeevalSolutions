# Solution for codeeval capitalized words problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '03-Mar-2015'

import sys

class CapitalizedWords():

	""" Solution for codeeval capitalized words problem """

	def __init__(self, filename):

		""" Initial function in CapitalizedWords class """

		self.filename = filename

	def read_file(self):

		""" Reads the inputfile and generates capitalized words as output """

		with open(self.filename, 'r') as f:
			for line in f:
				line = ' '.join(word[0].upper() + word[1:] for word in line.split())
				print line
				
def main():

	""" main function to create CapitalizedWords instance and get use of it """

	filename = sys.argv[1]
	capitalizeswords = CapitalizedWords(filename)
	capitalizeswords.read_file()

if __name__ == "__main__":
	main()