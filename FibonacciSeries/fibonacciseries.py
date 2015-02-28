# Solution for codeeval fibonacci series problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '28-Feb-2015'

import sys

class Fibonacci():

	""" Solution for codeeval fibonacci series problem  """

	def __init__(self, filename):

		""" Initial function in Fibonacci series class """

		self.filename = filename

	def readfile(self):

		""" Read the file input and take the inputs to our problem and generate output """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.get_fibonacci(int(line))

	def get_fibonacci(self, number):

		""" Generate fibonacci number for a given fibonacci number """

		self.number = number
		given_number = self.number

		if self.number == 0:
			return 0
		elif self.number == 1:
			return 1
		else :
			return self.get_fibonacci(given_number - 1) + self.get_fibonacci(given_number - 2)

def main():

	""" Main function to create Fibonacci class instance """

	filename = sys.argv[1]
	fibonacci = Fibonacci(filename)
	fibonacci.readfile()
if __name__ == "__main__":
	main()