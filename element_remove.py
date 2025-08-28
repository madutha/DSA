def removeElement(nums, val: int) -> int:
        elements = []
        for num in nums:
            if num != val:
                elements.append(num)
            else:
                pass
        elements.append("_")
        return elements
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))