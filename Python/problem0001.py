#File: Problem0001.py
#github.com/jbrdge

counter = 0
total = 0

while counter<1000:
	if counter%3 == 0 or counter%5 == 0:
		total += counter
	counter +=1

print(total)
