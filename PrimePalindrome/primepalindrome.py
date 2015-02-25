# Solution for codeeval primepalindrom problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '25-Feb-2015'

class PrimePalindrome():

	""" Solution for PrimePalindrome program """

	def __init__(self,number):

		""" Initial function in primepalindrom class """

		self.number = number

	def palindrome_check(self,primenumber):

		""" Checks the prime number and returns is it palindrome or not """

		self.primenumber = primenumber

		if self.primenumber == ''.join(reversed(self.primenumber)):
			return True
		else:
			return False

	def primepalindrome_generator(self):

		""" Return all the prime palindrome numbers with in the number range """

		primepalindrome_list = []		
		for num in xrange(2,self.number + 1):
			temp = []

			for i in xrange(2,num/2):
				temp.append(num%i)

			if temp.count(0) == 0 and self.palindrome_check(str(num)):
				primepalindrome_list.append(num)

			primepalindrome_list.sort()	
		
		return primepalindrome_list[-1]

def main():

	""" Main function to call PrimePalindrome class """

	number = 1000
	primepalinrome = PrimePalindrome(number)
	print primepalinrome.primepalindrome_generator()
if __name__ == "__main__":
	main()

