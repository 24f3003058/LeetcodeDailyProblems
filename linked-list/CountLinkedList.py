def count_rec(L, x):
    # Write your code here 
    count=0
    if not L:
        return 0
    current=L 
    if current.next==x:
        count+=1
    return count, count_rec(L[1:],x)