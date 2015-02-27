# Solution for codeeval sum of digits problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '26-Feb-2015'

import sys

class SumofDigits():

	""" Solution for codeeval sum of digits problem """

	def __init__(self,filename):

		""" Initial function in SumofDigits class """

		self.filename = filename

	def readfile(self):

		""" reads the input file """

		with open(self.filename, 'r') as f:
			
			for line in f:
				sum_value = sum([int(i) for i in str(line).replace("\n", "")])
				print sum_value
def main():

	""" Main Function to create SumofDigits class instance and get use of it """

	filename = sys.argv[1]
	result =SumofDigits(filename)
	result.readfile()

if __name__ == "__main__":
	main()
