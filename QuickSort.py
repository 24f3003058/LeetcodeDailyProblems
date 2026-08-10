def QuickSort(l,low,high):
    if low < high:

        pivot=l[low]
        i=low+1
        j=high

        while True:
            while (i <= j) and (l[i] <= pivot):
                i+=1

            while (i <=j) and (l[j] > pivot):
                j-=1 
            if i <= j:
                l[i],l[j] =l[j],l[i]
            else:
                break
        l[low],l[j]=l[j],l[low]
        QuickSort(l,low,j-1)
        QuickSort(l,j+1,high)

l=[14,23,8,55,1,41,18]
QuickSort(l,0,len(l)-1)
print(l)


    