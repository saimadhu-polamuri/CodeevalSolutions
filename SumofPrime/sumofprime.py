# Solution for codeeval sumofprime problem  

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '25-Feb-2015'

class SumOfPrime():

	""" Solution for codeeval sumofprime problem """

	def __init__(self,number):

		""" Initial function in SumOfPrime class """

		self.number = number

	def prime_check(self, num):

		""" Checks prime number validity for an given number """

		self.num = num
		remider_list = []
		for i in xrange(2,self.num):
			remider_list.append(self.num%i)
		# print remider_list.count(0)
		if remider_list.count(0) == 0:
			return True
		else:
			return False

	def prime_sum_generator(self):

		""" Generate prime number with in number range """
		
		prime_list = []
		prime_count = 0
		i = 2
		while(prime_count < self.number):

			if self.prime_check(i) :
				prime_list.append(i)
				prime_count += 1
				i += 1
			else:
				i += 1
		return sum(prime_list)

		
def main():

	""" Main function to create SumOfPrime instance """
	number = 1000
	primesum = SumOfPrime(number)
	print primesum.prime_sum_generator()
if __name__ == "__main__":
	main()