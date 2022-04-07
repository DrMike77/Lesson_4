from itertools import count, cycle
a = int(input("Ведите начальное число:"))
b = int(input("Ведите конечное число:"))
for el in count(a):
    if el > b:
        break
    print(el)
print("*" * 30)
n = [4, 8, 15, 16, 23, 42]
iterations_plan = 10
iteration_count = 0
for el in cycle(n):
    print(el)
    iteration_count += 1
    if iteration_count >= iterations_plan:
        break