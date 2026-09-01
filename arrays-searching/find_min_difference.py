def find_Min_Difference(L,P):
    L=sorted(L)
    min_diff=float('inf')
    for i in range(len(L) - P +1):
        diff=L[i + P -1] -L[i]
        min_diff=min(min_diff,diff)
    return min_diff
