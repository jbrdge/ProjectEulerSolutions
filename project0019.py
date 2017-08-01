#File: project0019.py

lengthdays = [True]*(((2000-1900)*365)+((2000-1900)/4)-1)


for i in range(0,len(lengthdays),1):
	if i%7!=0:
		lengthdays[i]=False


for i in range(0,len(lengthdays),1):
	if lengthdays[i] == True:
		print i
