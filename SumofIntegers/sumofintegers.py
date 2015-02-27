# Solution for codeeval sum of integers problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '27-Feb-2015'

import sys

class SumofIntegers():

	""" Solution for codeeval sum of integers problem  """

	def __init__(self,filename):

		""" Initial function in SumofIntegers class """

		self.filename = filename

	def readfile(self):

		with open(self.filename , 'r') as f:
			sum_value = sum([int(str(line).replace("\n", "")) for line  in f])
			print sum_value
			
def main():

	""" main function to create SumofIntegers instance and get use of it """

	filename = sys.argv[1]
	sumofintegers = SumofIntegers(filename)
	sumofintegers.readfile()

if __name__ == "__main__":
	main()

