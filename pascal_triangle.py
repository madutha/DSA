# def pascal_triangle(num_rows):
#     # If num_rows is 0, return empty list
#     if num_rows == 0:
#         return []
    
#     triangle = [[1]]  # First row is always [1]
    
#     # Build each row from the previous row
#     for i in range(1, num_rows):
#         prev_row = triangle[-1]       # Last row we built
#         new_row = [1]                  # Every row starts with 1
        
#         # Fill the middle elements using DP: sum of two elements above
#         for j in range(1, i):
#             new_row.append(prev_row[j - 1] + prev_row[j])
        
#         new_row.append(1)              # Every row ends with 1
#         triangle.append(new_row)       # Add row to triangle
    
#     return triangle

# # # Example: 5 rows
# # for row in pascal_triangle(5):
# #     print(row)
# print(pascal_triangle(5))


def pascal(nums):
    triangle = [[1]]

    for i in range(1,nums):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1,i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    return print(row) for in triangle
nums = 5
print(pascal(nums))