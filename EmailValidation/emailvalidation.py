# Solution for codeeval email validation problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '08-Mar-2015'

import sys
import re

class EmailValidation():

	""" Solution for codeeval email validation problem """

	def __init__(self,filename):

		""" Initial function in EmailValidation class """

		self.filename = filename

	def read_file(self):

		""" Reads the input file and gets the inputs for the E-mail validation """

		with open(self.filename, 'r') as f:
			for line in f:
				if len(line)>2:
					print self.get_emailvalidation(line)

	def get_emailvalidation(self,line):

		self.line = line.replace("\n", "")
		#if re.findall(r"\w+@\w+\.(?:com|in|org)",self.line):
		#if re.findall(r"\w+@\w+\.com",self.line):
		if not re.match(r"[a-z0-9]+@[a-z0-9]+.[a-z0-9]+", self.line):
			return 'false'
		else:
			return 'true'

def main():

	""" main function to create EmailValidation instance and get use of it """

	filename = sys.argv[1]
	emailvalidation = EmailValidation(filename)
	emailvalidation.read_file()

if __name__ == "__main__":
	main()

