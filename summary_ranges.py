def summary(nums):
    result = []
    start = nums[0]
    for i in nums:
        if i == len(nums)-1 or nums[i] +1== num[i+1]:
            result.append(str(start))
        if  




nums = [0,1,2,4,5,7]
print(summary(nums))