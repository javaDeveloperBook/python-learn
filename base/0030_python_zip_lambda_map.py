a = [1, 2, 3]
b = [4, 5, 6]

# zip 竖向组合
print(list(zip(a, b)))
print(list(zip(a, a, b)))

# lambda
fun1 = lambda x, y: x + y

# map
print(list(map(fun1, a, b)))
