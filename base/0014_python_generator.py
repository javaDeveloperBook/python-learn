print([x * x for x in list(range(10))])

g = (x * x for x in list(range(10)))
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e.value)
        break

print('-------------------------------')


def fibo(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'end'


f = fibo(10)

while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)
        break


print('-------------------------------')

for x in fibo(10):
    print(x)
