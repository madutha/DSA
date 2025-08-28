def singleNumber(self, nums: List[int]) -> int:
        
    
        if len(nums)==1:
            return nums[0]
        else:
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    if nums[j]> nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            
            short = nums
            
            for num in range(len(short)-1,-1,-2):
                if short[num] !=short[num-1]:
                    return short[num]
