# Solution for codeeval Right most char problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '06-Mar-2015'

import sys

class RightMost():

	""" Solution for codeeval Right most char problem  """

	def __init__(self,filename):

		""" Initial function in RightMost  class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and generates the input signals """

		with open(self.filename , 'r') as f:
			for line in f:
				if len(line) > 1:
					string_value , char_value = line.replace("\n", "").split(',')
					print string_value.find(char_value)

def main():

	""" main function to create RightMost class instance and get use of it """

	filename = sys.argv[1]
	rightmost = RightMost(filename)
	rightmost.read_file()

if __name__ == "__main__":
	main()