# 教程：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000
# 整数
print('100 + 200 =', 100 + 200)
print('0xff00 - 0xff00 =', 0xff00 - 0xff00)

# 浮点数
print('1.23e9 + 1.23e9 =', 1.23e9 + 1.23e9)

# 字符串
print('I\'m \"ok\"!')
print(r'\\\\\t\\\\n')
print('''line1
    ... line2
    ... line3''')

# 布尔值
print(True)
print(False)
print(3 > 2)
print(3 > 5)
print(True and False)
print(True or False)
print(not False)


# 空值
print(None)

# 变量(动态类型)，变量 a 的赋值不影响变量 b 的指向
a = 'ABC'
b = a
a = 123
print(a)
print(b)

# 常量，大写，仍然是一个变量，可变，不可保证不会被改变
PI = 3.14159265359
print(PI)
PI = 1
print(PI)

# 整数除法为什么是精确的
print(10/3)
# 地板除，两个整数的除法仍然是整数,只取结果的整数部分
print(10//3)
# 取余
print(10 % 3)




