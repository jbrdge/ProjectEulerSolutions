#File: Prioject0003.py

number=600851475143
number_list=[]

def is_prime(n):
	if n%2==0 and n != 2:
		return 0
	else:
		j=3
		while j<n/2:
			if n%j==0:
				return 0 
			j+=2


if number%2==0:
	number_list.extend([2])

i=3
while i<= number:
	if number%i==0:
		number = number/i
		number_list.extend([i])
	i+=2

for i in number_list:
	if is_prime(i)==0:
		number_list.remove(i)

print number_list[-1]
