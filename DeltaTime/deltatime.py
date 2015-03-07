# Solution for codeeval delta time problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '07-Mar-2015'

import sys
from dateutil import parser
class DeltaTime():

	""" Solution for codeeval delta time problem  """

	def __init__(self,filename):

		""" Initial function in DeltaTime class """

		self.filename = filename

	def read_file(self):

		""" Reads the text file and gets the inputs for solving problem """

		with open(self.filename , 'r') as f:
			for line in f:
				print self.get_timedifference(line)

	def get_timedifference(self,line):

		""" Converts the line into two times and get the difference between them """

		self.line = line.replace("\n", "")
		timedifference = str(self.get_datetime(max(self.line.split())) - self.get_datetime(min(self.line.split())))
		if int(timedifference.split(':')[0])<10:
			return '0'+timedifference
		else :
			return timedifference

	def get_datetime(self,date):

		""" converts the string to datetime """

		self.date = date

		result = parser.parse(self.date,dayfirst=True)
		return result

def main():

	filename = sys.argv[1]
	deltatime = DeltaTime(filename)
	deltatime.read_file()

if __name__ == "__main__":
	main()