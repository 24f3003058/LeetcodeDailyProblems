L=[1,24,53,5,6,20]

def SelectionSort(L):
    for i in range(len(L)):
        min_idx=i
        for j in range(i+1, len(L)):
            if L[j] < L[min_idx]:
                min_idx= j
        L[i] ,L[min_idx] =L[min_idx] ,L[i]
    return L

L=[12,18,7,3,5,7,7]
print(L)
print(SelectionSort(L))
