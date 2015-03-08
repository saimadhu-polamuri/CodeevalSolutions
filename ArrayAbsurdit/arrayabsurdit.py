# Solution for codeeval array absurdit problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '08-Mar-2015'

import sys

class ArrayAbsurdit():

	""" Solution for codeeval array absurdit problem  """

	def __init__(self,filename):

		""" Initial function in ArrayAbsurdit class """

		self.filename = filename

	def read_file(self):

		""" reads the input file and get the inputs to solve problem """

		with open(self.filename, 'r') as f:
			for line in f:
				if len(line)>1:
					lenght_value,array_values = line.split(';')
					list_values = [int(x) for x in array_values.split(',')]
					print self.get_arraysurdit(list_values)

	def get_arraysurdit(self,list_values):

		""" find the arraysurdit value from an given list """

		self.list_values = list_values
		set_values = set([x for x in self.list_values if self.list_values.count(x) > 1])
		return list(set_values)[0]

def main():

	""" main function to create ArrayAbsurdit instance and get use of it """

	filename = sys.argv[1]
	arrayabsurdit = ArrayAbsurdit(filename)
	arrayabsurdit.read_file()

if __name__ == "__main__":
	main()