def majority(nums):
    can = None
    count = 0
    for i in nums:
        if count == 0 :
            can = i
        count += (1 if i == can else -1)
    return can
            

nums = [2,2,1,1,1,2,2]
print(majority(nums))