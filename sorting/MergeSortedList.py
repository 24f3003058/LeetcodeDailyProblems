def merge_arrays(nums1, nums2):
    # Write your code here
    mergedList=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] <= nums2[j]:
            mergedList.append(nums1[i])
            i+=1             
        else:
            mergedList.append(nums2[j])
            j+=1
    mergedList.extend(nums1[i:])
    mergedList.extend(nums2[j:])       
    return mergedList   
              
     
           
       
       
       
       