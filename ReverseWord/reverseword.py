# Solution for codeeval Reverse words problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '26-Feb-2015'

import sys

class ReverseWords():

	""" Solution for codeeval Reverse words problem """

	def __init__(self,filename):

		""" Initial function in ReverseWords class """

		self.filename = filename
		
	def print_oneline(self,list_values):

		""" prints list in one line """

		self.list_values = list_values

		print(" ".join(str(x) for x in self.list_values)) 

	def readfile(self):

		with open(self.filename, 'r') as f:
			
			for line in f:
				if len(line) >1:
					words_list = line.split()
					words_list.reverse()
					self.print_oneline(words_list)

def main():

	""" Main Function to create ReverseWords instance and get use of it """

	filename = sys.argv[1]
	reversewords = ReverseWords(filename)
	reversewords.readfile()
if __name__ == "__main__":
	main()


