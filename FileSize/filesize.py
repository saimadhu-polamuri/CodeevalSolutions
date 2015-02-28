# Solution for codeeval File size problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '28-Feb-2015'

import sys
import os

class FileSize():

	""" Solution for codeeval File size problem """

	def __init__(self,filename):

		self.filename = filename
		
	def get_filesize(self):

		return os.path.getsize(self.filename)
def main():

	filename = sys.argv[1]
	filesize = FileSize(filename)
	print filesize.get_filesize()

if __name__ == '__main__':
	main()


