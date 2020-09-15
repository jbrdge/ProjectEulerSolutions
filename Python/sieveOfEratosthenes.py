#sieve of eratosthenes
import numpy as np

#define max integer value n
n=10209
A = [True]*(n)
B = []


for i in range(2,int(np.sqrt(n))):
    if A[i]==True:
        j = i**2
        while j<n:
            A[j] = False
            j = j + i

for i in range(2,len(A)):
    if A[i]==True:
        B.append(i)
        
print(B)