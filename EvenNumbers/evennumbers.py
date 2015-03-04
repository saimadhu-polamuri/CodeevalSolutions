# Solution for codeeval even numbers problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '03-Mar-2015'

import sys

class EvenNumbers():

	""" Solution for codeeval even numbers problem  """

	def __init__(self,filename):

		""" Initial function in EvenNumbers class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and generates the output """

		with open(self.filename, 'r') as f:
			for line in f:
				if int(line)%2 == 0:
					print 1
				else:
					print 0

def main():

	""" main function to create EvenNumbers instance and get use of it """

	filename = sys.argv[1]
	evennumber = EvenNumbers(filename)
	evennumber.read_file()

if __name__ == "__main__":
	main()