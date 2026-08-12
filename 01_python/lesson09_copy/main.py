# a = [1, 2, 3]

# b = a.copy()
# print(id(a))
# print(id(b))

# matrix = [
#     [1,2],
#     [3,4]
# ]

# copy_matrix = matrix.copy()
# copy_matrix[0][0] = 100

# print(matrix)
# print(copy_matrix)

import copy

matrix = [
    [1, 2],
    [3, 4]
]

new_matrix = copy.deepcopy(matrix)
new_matrix[0][0] = 999

print(matrix)
print(new_matrix)