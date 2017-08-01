#File: project0005.py

j=999
i =j/2
pal_list=[]

def is_palin(a):

	forwards = map(int, str(a))
	backwards = list(reversed(forwards))

	if forwards == backwards:
		return 1
	else:
		return 0
while i<j:
	n=i	
	while n<=j:
		a= n*j
		if a%11==0:
			if is_palin(a):
				pal_list.append(a)
		n+=1
	i+=1
	j-=1

pal_list.sort()
print pal_list[-1]
	
