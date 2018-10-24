'''								
  * Problem 25 - Project Euler 	*
  * Jacob Breckenridge 			*
  * 10/24/18					*
  *								*
'''

import numpy as np
'''
program determines the next fibbonocci number until the number is a specified length,
prints out the index and a string version of the number because it will not be able to 
store values with too many digits
'''
#note if we consistently order a<b then len(a)<=len(b)
def add_strings(a,b):
	n=0
	c=[]
	temp=b
	while(len(a)<len(b)):
		a.insert(0,'0')
		n+=1
	for i in range(len(a)-1,-1,-1):
		if len(str(int(a[i])+int(temp[i])))==2:
			c.insert(0,str(int(a[i])+int(temp[i])))
			b[i-1] = str(int(temp[i-1]))
		else:
			c.insert(0,str(int(a[i])+int(temp[i])))
	while n>0:
		del a[0]
		n-=1
	return c


if __name__ == '__main__':
	length=1000
	F1=['1']
	F2=['1']
	Fibb = [F1,F2]
	i=0
	count=2
	while(True):
		count+=1
		if(len(list(add_strings(Fibb[i-2],Fibb[i-1]))[0])==length):
			print(list(add_strings(Fibb[i-2],Fibb[i-1])))
			print(count)
			break
		Fibb+=[add_strings(Fibb[i-2],Fibb[i-1])]
	
