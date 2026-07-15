def FindPeak(L):
  left ,right=0,len(L) -1
  while left< right:
    mid=(left+right)//2
    if L[mid] > L[mid +1]:
      right=mid
    else:
      left=mid+1
  return L[left]
