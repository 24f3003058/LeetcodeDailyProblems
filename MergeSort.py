def merge(L1,L2):
    m,n=len(L1),len(L2)
    new_L=[]
    i,j=0,0

    while (i<m) and (j<n):
        if L1[i] <= L2[j]:
            new_L.append(L1[i])
            i += 1
        else:
            new_L.append(L2[j])
            j +=1
    while i < m :
        new_L.append(L1[i])
        i += 1
    while j< n:
        new_L.append(L2[j])
        j+=1 
    return new_L
def merge_sort(L):
    l= len(L)
    if l <= 1:
        return L
    left=merge_sort(L[:(l//2)])
    right=merge_sort(L[(l//2):])
    final_L=merge(left,right)

    return final_L

print(merge_sort([12,43,2,44,33,22,300]))
