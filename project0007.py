import math

def is_prime(a):
  for x in range(2,int(math.sqrt(a))+2):
    if a%x==0:
      return 0
      break
  return 1

primelist = [2]

n=2
while len(primelist)<10001:
  if is_prime(n):
    primelist.append(n)
  n+=1

print primelist 
  
