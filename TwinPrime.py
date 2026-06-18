def Twin_Primes(n,m):
    def isPrime(n):
        if n<2:
           return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    result=[]
    
    for num in range(n,m-1):
        if (isPrime(num) and isPrime(num +2)):
            if num+2 <=m:
                result.append((num,num+2))
                
    return result
