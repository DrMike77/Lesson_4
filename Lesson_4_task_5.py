from functools import reduce

n = [item for item in range(100, 1000 + 1) if item % 2 == 0]
print(n)
m = reduce(lambda x, y: x * y, n)
v = reduce(lambda x, y: x * y, n, 1)
print(m)
print(v)
if m == v: print("good")