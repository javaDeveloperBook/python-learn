print(abs(-100))

print(max(1, 2, 10, -20))

h = hex
print(h(100))


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operate type.')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(0))
print(my_abs(-1))


# print(my_abs('A'))


# 定义空函数
def nop():
    pass


# 返回多个值,返回值是一个 tuple
def return_two(x, y):
    return x * 2, y * 2


print(return_two(1, 2))


# 计算多次方
def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(5, 3))
print(power(5))


# 默认参数的坑
def add_end(ls=[]):
    ls.append('END')
    return ls


print(add_end())
print(add_end())
print(add_end())


def add_end2(ls=None):
    if ls is None:
        ls = []
    ls.append('END')
    return ls


print(add_end2())
print(add_end2())
print(add_end2())


# 可变参数,参数 nums 接收到的是一个tuple
def calc(*nums):
    s = 0
    for n in nums:
        s += n * n
    return s


# print(calc([1, 2, 3, 4]))
print(calc(1, 2, 3, 4))
print(calc())
nums = [2, 3, 4]
print(calc(*nums))


# 关键字参数
def person(name, age, **extra):
    print('name:', name, ' age:', age, ' extra:', extra)


person('jack', 25, **{'jab': 'java', 'city': 'ChongQi'})
