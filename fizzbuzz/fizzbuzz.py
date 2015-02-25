# Solution for codeeval fizzbuzz problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '25-Feb-2015'

import sys

class FizzBuzz():

	""" FizzBuzz problem solution """

	def __init__(self, filename):

		""" Initial funtion in FizzBuzz class """

		self.filename = filename
	
	def number_check(self,number,x,y):

		""" Checks to number and returns fizzbuzz pattern for that number """

		self.number = number
		self.x = self.x
		self.y = self.y

		if self.number % self.x == 0 and self.number % self.y == 0:
			pattern =  'FB'
		elif self.number % self.x == 0:
			pattern = 'F'
		elif self.number % self.y == 0:
			pattern = 'B'
		else:
			pattern = number

		return pattern

	def fizzbuzz_pattern(self,x,y,z):

		""" Returns the fizzbuzz pattern for the input pattern """

		self.x = x
		self.y = y
		self.z = z
		pattren_list = []
		for i in xrange(1,self.z + 1):
			pattren_list.append(self.number_check(i,self.x,self.y))

		return pattren_list

	def print_oneline(self,list_values):

		""" prints list in one line """

		self.list_values = list_values

		print(" ".join(str(x) for x in self.list_values)) 

	def read_file(self):

		""" Reads the input file and generates inputs for fizzbuzz problem """

		with open(self.filename, 'r') as f:
			for line in f:
				input_values = line.split()
				x = int(input_values[0])
				y = int(input_values[1])
				z = int(input_values[2])
				temp = self.fizzbuzz_pattern(x,y,z)
				self.print_oneline(temp)

def main():                                                       

	""" Main function for FizzBuzz class """

	filename = sys.argv[1]
	fizzbuzz = FizzBuzz(filename)
	fizzbuzz.read_file()

if __name__ == "__main__":
	main()