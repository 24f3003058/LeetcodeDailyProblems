def factor(n):
    factorlist=[]
    for i in range(1,n+1):
        if n%i==0:
            factorlist.append(i)
    return factorlist
    
def is_prime(n):
    return (len(factor(n))==2)
    
def prime_product(n):
    if n<0:
        return False
    primelist=[]
    
    for i in range(n):
        if is_prime(i):
            primelist.append(i)
    for i in range(len(primelist)):
        for j in range(i,len(primelist)):
            if (primelist[i]*primelist[j])==n:
                return True
            
        return False

n = int(input())
print(prime_product(n))
