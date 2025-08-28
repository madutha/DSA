def two_sum(arr, target):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

nums = [2,7,11,15]
target = 26

print(two_sum(nums, target))