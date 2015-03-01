# Solution for codeeval unique elements problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '1-Mar-2015'

import sys

class UniqueElements():

	"""  Solution for codeeval unique elements problem  """

	def __init__(self,filename):

		""" Initial Function in UniqueElements class """

		self.filename = filename

	def input_extraction(self,line):

		""" Extracts input sequence from a given line """

		self.line = line.replace("\n", "")
		return (list(set(self.line)))
		# list_value = self.line.split(',')
		# set_values = list(set([int(i) for i in list_value]))
		#return (",".join(str(x) for x in set_values))

	def read_file(self):

		""" Read the input file return the unique elements """

		with open(self.filename, 'r') as f:
			for line in f:
				print self.input_extraction(line)

def main():

	""" main function for creating UniqueElements class instance """

	filename = sys.argv[1]
	uniqueelements = UniqueElements(filename)
	uniqueelements.read_file()

if __name__ == "__main__":
	main()