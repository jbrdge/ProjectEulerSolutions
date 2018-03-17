#File: project0021.py
import numpy as np
#this program determines all of the amicable numbers under a given value
'''
#Let d(n) be defined as the sum of proper divisors of n
#(numbers less than n which divide evenly into n)
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
#and each of a and b are called amicable numbers
'''

def sum_prop(n):
    A = [True]*(n)
    prime_divisors = []    
    for i in range(2,int(np.sqrt(n))):
        if A[i]==True:
            j = i**2
            while j<n:
                A[j] = False
                j = j + i
                
    for i in range(2,len(A)):
        if A[i]==True and n%i==0:
            prime_divisors.append(i)
                        
    proper_divisors = []
    for i in prime_divisors:
        k = i
        while k<n:
            if n%k==0:  
                proper_divisors.append(k)
                k = k+i
            else:
                k=k+i
    proper_divisors = [1] + list(set(proper_divisors))
    pd_sum = 0
    for i in proper_divisors:
        pd_sum = pd_sum + i 
                                            
    return pd_sum     
    
total = 0
A = list(range(10000))
for i in A:
    if i ==sum_prop(sum_prop(i)) and i !=sum_prop(i):
        print(i)
        total = total + i
print(total)
