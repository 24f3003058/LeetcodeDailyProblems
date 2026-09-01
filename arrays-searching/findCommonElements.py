def findCommonElements(L1,L2):
    new_list=[]
    for i in range(len(L1)):
        if L1[i]  in L2:
            new_list.append(L1[i])
    return selectionSort(new_list)
def selectionSort(new_list):
    for i in range(len(new_list)):
        min_idx=i
        for j in range(i+1,len(new_list)):
            if new_list[j] <new_list[min_idx]:
                min_idx=j

        new_list[i],new_list[min_idx]=new_list[min_idx],new_list[i]
    return new_list



L1=[23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
L2=[23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]

print(findCommonElements(L1,L2)) 