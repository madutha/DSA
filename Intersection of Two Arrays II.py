def intersection(nums1,nums2):
    result = []
    nums1.sort()
    nums2.sort()
    P,q = 0,0
    while P < len(nums1) and q < len(nums2):
        if nums1[P] == nums2[q]:
            result.append(nums1[P])
            P+=1
            q+=1
        elif nums1[P] < nums2[q]:
            P+=1
        else:
            q+=1
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))