n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
x = [val for i, val in enumerate(n)
    if i > 0 and n[i - 1] < val]
print(x)