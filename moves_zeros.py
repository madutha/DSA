def moveszeros(nums):
    
    p = 0
    for i in nums:
        if nums[p] ==  0:
            nums.pop(p)
            nums.append(0)
        p += 1 if nums[p] != 0 else 0
            
    return nums


nums = [0,1,0,3,12]
print(moveszeros(nums))