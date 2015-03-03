# Solution for codeeval sort of numbers problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '02-Mar-2015'

import sys

class SortNumbers():

	""" olution for codeeval sort of numbers problem  """

	def __init__(self,filename):

		""" Initial function in SortNumbers class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and gets the input numbers and later it will sort these numbers """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.line_sort(line)
	def line_sort(self, line):

		""" Returns the sorted list for a given line """

		self.line = line.split()

		line_list = [float(i) for i in self.line]
		line_list.sort()

		return (" ".join('%.3f' % x for x in line_list))

def main():

	""" main function to create SortNumbers instances and get use of it """

	filename = sys.argv[1]
	sortnumbers = SortNumbers(filename)
	sortnumbers.read_file()

if __name__ == "__main__":
	main()
