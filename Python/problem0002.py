#File: Problem0002.py
#github.com/jbrdge

first_term = 1
second_term = 2
total_sum = 0
def fib(a,b,n):
	sum = a
	if b < n:
		sum+=fib(b,a+b,n)
		if a%2==1:
			sum-=a
	return sum

print(fib(1,1,4000000))
