# Solution for codeeval set intersection problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '1-Mar-2015'

import sys

class SetIntersection():

	""" Solution for codeeval set intersection problem """

	def __init__(self, filename):

		""" Initial function in SetIntersection class """

		self.filename = filename

	def list_extraction(self,single_line):

		""" extracts two list from single line on text """

		self.single_line = single_line
		set1,set2 = self.single_line.split(';')
		return set1,set2

	def line_to_intersectionset(self,line):

		""" generates two sets from a given line """

		self.line = line.replace("\n", "")

		set1,set2 = self.line.split(';')
		set1_list = [int(i) for i in set1.split(',')]
		set2_list = [int(i) for i in set2.split(',')]
		unique_list = list(set(list(set1_list)).intersection(list(set2_list)))
		return (",".join(str(x) for x in unique_list))

	def print_oneline(self,list_values):

		""" prints list in one line """

		self.list_values = list_values

		return (",".join(str(x) for x in self.list_values)) 

	def read_file(self):

		""" Reads input file and generates input for calling list_extraction function """

		with open(self.filename, 'r') as f:
			for line in f:
				
				print self.line_to_intersectionset(line)

def main():

	""" main function to create SetIntersection instances and get use of it """

	filename = sys.argv[1]
	setintersection = SetIntersection(filename)
	setintersection.read_file()

if __name__ == "__main__":
	main()