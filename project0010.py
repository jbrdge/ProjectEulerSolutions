import math
n=2000000
primelist= [2]



for i in range(3,n,2):
	for j in primelist:
		if i%j==0:
			break
		if j>math.sqrt(i):
			primelist.append(i)
			break
		

summ=0
for a in primelist:
	summ+=a
print summ
