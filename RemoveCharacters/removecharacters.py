# Solution for codeeval remove characters problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '03-Mar-2015'

import sys
import re

class RemoveCharacters():

	""" Solution for codeeval remove characters problem  """

	def __init__(self,filename):

		""" Initial function in RemoveCharacters class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and removes the specific characters """

		with open(self.filename, 'r') as f:
			for line in f:
				string1,string2 = line.split(',')
				print self.removed_string(string1,string2)

	def removed_string(self,string1,string2):

		""" removes the occurrence of string2 in string1 """
		self.string2 = string2
		removed_words = [word.translate(None,self.string2) for word in string1.split()]
		
		return (" ".join(x for x in removed_words))

def main():

	""" main function to create RemoveCharacters instance and get use of it """

	filename = sys.argv[1]
	removecharacters = RemoveCharacters(filename)
	removecharacters.read_file()

if __name__ == "__main__" :
	main()