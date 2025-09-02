def intersection(nums1,nums2):
        result = []
        p = 0
        while p < len(nums2):
            if nums2[p] in nums1:
                result.append(nums2[p])
                p+=1
            else:
                p+=1
        return list(set(result))
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))

