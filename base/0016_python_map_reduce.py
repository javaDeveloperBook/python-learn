# map() 函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
from functools import reduce


def power(x):
    return x * x


# print(list(map(power, [1, 2, 3, 4, 5])))
# print(list(map(str, [1, 2, 3, 4, 5])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

reduce(power, [1, 2, 3])

