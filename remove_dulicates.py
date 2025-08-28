def removeDuplicates(nums):
    if len(nums)==0:
        return 0

    j = 0

    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))