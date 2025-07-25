
def calculate_avg(arr):
    sum = 0
    for num in arr:
        sum = num + sum
    return sum/len(arr)
    
arr = [1,2,3,4,5,3,]
avg_num = calculate_avg(arr)
print(avg_num)