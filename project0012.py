import math

def divisor_list(x):
  dlist=[]
  for i in range(1,int(math.sqrt(x))+1):
    if x%i==0:
      dlist.append(i)
      dlist.append(x/i)
  return dlist


n=1

while len(divisor_list(n*(n+1)/2))<500:
  n+=1

print n*(n+1)/2
