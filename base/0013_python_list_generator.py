import os

print([x * x for x in list(range(1, 11))])

print([x * x for x in list(range(1, 11)) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'DEF'])

print(list(zip(['A', 'B', 'C'], ['D', 'E', 'F'])))

print([d for d in os.listdir('.')])
