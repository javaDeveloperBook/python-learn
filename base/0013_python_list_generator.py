import os

print([x * x for x in list(range(1, 11))])

print([x * x for x in list(range(1, 11)) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'DEF'])

print([d for d in os.listdir('.')])

