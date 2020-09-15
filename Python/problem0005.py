#project0005
#github.com/jbrdge

def smallest_multiple(number):

    a = list(range(2,number+1))
    n = 1

    for i in range(0,len(a)):
        for j in range(i-1,-1,-1):
            if(a[i]%a[j]==0):
                a[i]=a[i]//a[j]
    for i in a:
        n*=i
    return(n)

print(smallest_multiple(20))
