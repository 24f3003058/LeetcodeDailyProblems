def InsertionSort(l):
    n=len(l)
    if n<1:
        return l
    for i in range(n):
        j=i
        while(j>0 and l[j] <l[j-1]):
            l[j],l[j-1]=l[j-1],l[j]
            j -=1
    return l

print(InsertionSort([12,23,45,3,3,5,31]))
    