def fact (number: int):
    t = 1
    if number <= 0:
        yield t
    for x in range(1, number + 1):
        t *= x
        yield t
N = 4
for el in fact(N):
    print(el)