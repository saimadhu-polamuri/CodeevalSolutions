# Solution for codeeval sumofprime problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '25-Feb-2015'

class OddNumbers():

	""" Solution for codeeval sumofprime problem """

	def get_oddnumbes(self):

		""" Generates odd numbers from 1 to 99 """

		
		for i in xrange(1,100):
			if i%2 !=0:
				print i

def main():

	""" main function to create OddNumbers instance and get use of it """

	oddnumbers = OddNumbers()
	oddnumbers.get_oddnumbes()

if __name__ == "__main__":
	main()