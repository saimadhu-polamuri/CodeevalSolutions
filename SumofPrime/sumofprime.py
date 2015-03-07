# Solution for codeeval sumofprime problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '25-Feb-2015'

from math import sqrt

class SumOfPrime():

	""" Solution for codeeval sumofprime problem """

	def __init__(self,number):

		""" Initial function in SumOfPrime class """

		self.number = number

	def is_prime(self,num):

		self.num = num
		result = all(self.num % i for i in xrange(2, self.num))
		return result

	def prime_sum_generator(self):

		""" Generate prime number with in number range """
		
		prime_list = []
		prime_count = 0
		i = 2
		while(prime_count < self.number):

			if self.is_prime(i) :
				prime_list.append(i)
				prime_count += 1
				i += 1
			else:
				i += 1
		return sum(prime_list)

		
def main():

	""" Main function to create SumOfPrime instance """

	primesum = SumOfPrime(1000)
	print primesum.prime_sum_generator()
if __name__ == "__main__":
	main()