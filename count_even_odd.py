def countevenodd(arr):
    counteven = 0
    countodd = 0
    for num in arr:
        if num%2 == 0:
            counteven += 1
        else:
            countodd += 1
    return {
        "even_count" : counteven, 
        "odd_count" : countodd
    }

arr = [1,2,3,4,6,5,3]
ans = countevenodd(arr)
print(ans)
