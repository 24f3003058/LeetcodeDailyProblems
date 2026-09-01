def BubbleSort(L):
    n=len(L)

    for i in range(len(L)):
       swapped=False
       for j in range(0,n-i-1):
           if L[j] >L[j+1]:
               L[j], L[j+1]=L[j+1],L[j]
               swapped=True 
       if not swapped:
           break
    return L

L=[10,5,65,7,40]
print(BubbleSort(L))   