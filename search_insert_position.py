def search_postion(nums,target):
    for i in range(len(nums)):
        if nums[i]>= target:
            return i
        
    return len(nums)

nums = [1,3,5,6]
target = 7

print(search_postion(nums,target))