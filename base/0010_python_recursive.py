def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(10))
print(fact(100))
# 栈溢出，优化：改成尾递归方式，python 没有优化还是会栈溢出
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
print(fact(1000))
