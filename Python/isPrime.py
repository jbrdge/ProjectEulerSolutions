#is_prime
#github.com/jbrdge
def is_prime(n):
    '''Determines if int is prime'''
    if n%2==0 and n!=2:
        return(0)
    else:
        j=3
        while j<n/2:
            if n%j==0:
                return(0) 
        j+=2
