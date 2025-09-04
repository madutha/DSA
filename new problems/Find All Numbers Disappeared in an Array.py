def findDisappearedNumbers(nums):
    # for num in nums:
    #     indexing = abs(num) -1
    #     if nums[indexing] > 0:
    #         nums[indexing] = -nums[indexing]
    #     result = []

    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             result.append(i+1)
    #     return result
    n = len(nums)
    num_set = set(nums) 
    result = []
    for i in range(1, n+1):
        if i not in num_set:
            result.append(i)
    return result



nums = [1,1]
print(findDisappearedNumbers(nums))