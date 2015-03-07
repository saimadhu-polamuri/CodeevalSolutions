# Solution for codeeval Longest line problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '07-Mar-2015'

import sys

class LongestLine():

	""" Solution for codeeval Longest line problem """

	def __init__(self,filename):

		""" Initial function in LongestLine class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and the inputs from the input file """
		string_list = []
		with open(self.filename , 'r') as f:
			number_value = int(f.readline())
			for line in f:
				string_list.append(line.replace("\n", ""))

			string_list.sort(key=len)
			string_list.reverse()
			for single_string in string_list[:number_value]:
				print single_string

def main():

	""" main function to create LongestLine class instance and get use of it """

	filename = sys.argv[1]
	logestline = LongestLine(filename)
	logestline.read_file()

if __name__ == "__main__":
	main()
