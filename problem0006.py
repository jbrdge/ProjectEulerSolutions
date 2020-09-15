def nSum(n):
    return (n+1)*(n)//2

def sumSquareDiff(n):
    sum = 0
    for i in range(2,n):
        sum+=99*2*nSum(i-1)
    return(sum)

print(sumSquareDiff(100))