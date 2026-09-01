def SortInRange(L,r):
    count=[0 for _ in range(r)]
    for x in L:
        count[x]+=1

    idx=0
    for value in range(r):
        for _ in range(count[value]):
            L[idx] =value
            idx+=1
    return L

L=[2,0,1,1,2,3,0,2,1,0,2,3,1,2]
r=4
print(SortInRange(L,r))

