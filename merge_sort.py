def merge_sort(list1,list2):
    sorted = []
    i = j= 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted.append(list1[i])
            i+= 1
        else:
            sorted.append(list2[j])
            j+= 1
    sorted.extend(list1[i:])
    sorted.extend(list2[j:])
    return sorted
list1 = [1,2,4]
list2 = [1,3,4]

print(merge_sort(list1,list2))

# p