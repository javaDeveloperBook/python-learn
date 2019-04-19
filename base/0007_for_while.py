# for...in 循环
students = ['Jack', 'Tom', 'Mike']
for name in students:
    print(name)

sum = 0
for num in list(range(101)):
    sum += num
print(sum)

# while
sum2 = 0
n = 100
while n > 0:
    sum2 += n
    n = n - 1
print(sum2)

# break
i = 20
while i > 0:
    if i < 10:
        break
    print(i)
    i = i - 1

# continue
j = 0
while j < 20:
    j = j + 1
    if j % 2 == 0:
        continue
    print(j)










