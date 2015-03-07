# Solution for codeeval swap elements problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '07-Mar-2015'

import sys

class SwapElements():

	""" Solution for codeeval swap elements problem """

	def __init__(self,filename):

		""" Initial function in SwapElements class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and geneartes the inputs """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.convert_inputs(line)


	def convert_inputs(self,line):

		""" Converts txt line to useful inputs to solve our problem """

		self.line = line.replace("\n", "")
		integers,swapintegers = line.split(':')
		integer_list = [int(x) for x in integers.split()] 
		swap_set_integers = swapintegers.split(',')
		swapset1 = []
		swapset2 = []
		for singleset in swap_set_integers:
			number1,number2 = singleset.replace(" ", "").split('-')
			swapset1.append(int(number1))
			swapset2.append(int(number2))
		
		return self.swap_elements(integer_list,swapset1,swapset2)

	def swap_elements(self,integer_list,swapset1,swapset2):

		""" swaps the integer_list elements based on swapset1,swapset2 lists """

		self.swapset1 = swapset1
		self.swapset2 = swapset2

		for i in xrange(0,len(self.swapset1)):

			temp = integer_list[swapset1[i]]
			integer_list[swapset1[i]] = integer_list[swapset2[i]]
			integer_list[swapset2[i]] = temp

		#return integer_list
		return (" ".join('%d' % x for x in integer_list))			

def main():

	""" Main function to create SwapElements instance """

	filename = sys.argv[1]
	swapelements = SwapElements(filename)
	swapelements.read_file()

if __name__ == "__main__":
	main()
