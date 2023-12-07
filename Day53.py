# map(),filter(),reduse()
from functools import reduce

# MAP
# def cube(x):
#     return x * x * x

# l = [1, 2, 3, 4, 5, 6]

# print(list(map(cube, l)))

# FILTER

# newL = [1, 2, 3, 4, 5, 6]

# print(list(filter(lambda x: x > 2, newL)))

# REDUCE

newL = [1, 2, 3, 4, 5, 6]

print(reduce(lambda x, y: x + y, newL))
