def hcf(x,y):
    cf=[]
    for i in range(1, min(x,y) +1):
        if (x % i)==0 and (y % i)==0:
            cf.append(i)
    print(cf)
    return(cf[-1])

print(hcf(6,12))
