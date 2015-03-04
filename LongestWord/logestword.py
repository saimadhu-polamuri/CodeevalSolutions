# Solution for codeeval Logest word problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '03-Mar-2015'

import sys

class LogestWord():

	"""  Solution for codeeval Logest word problem  """

	def __init__(self,filename):

		""" Initial function in LogestWord class """

		self.filename = filename

	def read_file(self):

		""" Reads the inputfile and returns logest word """

		with open(self.filename, 'r') as f:
			for line in f:
				words = line.split()
				print max(words,key=len)
def main():

	""" main function to create LogestWord instance """

	filename = sys.argv[1]
	logestword = LogestWord(filename)
	logestword.read_file()

if __name__ == "__main__":
	main()