a=21
b=10
#算术运算符
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)
print('a//b=',a//b)
print('a**b=',a**b)

#比较运算符
print("a==b : ",a==b)
print("a!=b : ",a!=b)
print("a>b : ",a>b)
print("a<b : ",a<b)
print("a>=b : ",a>=b)
print("a<=b : ",a<=b)

#位运算符
c=60
d=13
print('c&d=',c&d)
print('c|d=',c|d)
print('c^d=',c^d)
print('~c=',~c)
print('c<<2=',c<<2)
print('c>>2=',c>>2)

b1=b2=True
b3=b4=False
#逻辑运算符
print("true and true : " ,b1 and b2)
print("true and false : " ,b1 and b3)
print("false and false : " ,b3 and b4)
print("true or false : " ,b1 or b3)
print("false or false : " ,b3 or b4)
print("true not : " ,not b1)
print("false not : " ,not b3)

#成员运算符
list=[1,2,3,4,5]
print(1 in list)
print(1 not in list)

#身份运算符
'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
x=20
y=20
print(x is y)
y=30
print(x is not y)


