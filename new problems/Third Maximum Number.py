def thirdmax(nums):
    distinct = list(dict.fromkeys(nums))
    if len(distinct) >= 3:
        sorted_list = sorted(distinct, reverse= True) [2]
        return sorted_list
    else:
        return max(distinct)
    

nums = [1,2,2,5,3,5]
print(thirdmax(nums))