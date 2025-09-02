def merge(nums1,nums2):
    nums1.extend(nums2)
    while 0 in nums1:
        nums1.remove(0)
    return sorted(nums1)


nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
print(merge(nums1,nums2))