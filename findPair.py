def findPair(L,pairsum):
      for i in range(len(L)) :
           for j in range(len(L)):
                if (L[i]+L[j]) == pairsum:
                    return True
           return False

L = [int(item) for item in input().split()] 
pairsum = int(input()) 
print(findPair(L, pairsum))