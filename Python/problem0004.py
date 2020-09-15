#File: Problem0004.py
#github.com/jbrdge

from isPalindrome import is_palindrome

j=999
i=int(j/10)
pal_list=[]
while i<j:
	n=i	
	while n<=j:
		a= n*j
		if a%11==0:
			if is_palindrome(a):
				pal_list.append(a)
		n+=1
	i+=1
	j-=1

pal_list.sort()
print (pal_list[-1])
	
