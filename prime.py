

def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True      

def twinPrimes(n,m ):

    twins=[]

    for i in range(n,m+1):
        if (i+2 <=m ):
            if isprime(i) and isprime(i+2):
               twins.append((i,i+2))
    return twins

print(twinPrimes(1,15))

