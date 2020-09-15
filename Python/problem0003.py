#File: Problem0003.py
#github.com/jbrdge

from isPrime import is_prime

def largestPrimeFactor(number):
	if number==2:
		return 2
	else:
		i=2
		while number%i==0:
			number = number//i
		i=3
		while i<number:
			while number%i==0:
				number = number//i
			i+=2
		print(i)	


number=600851475143
largestPrimeFactor(number)