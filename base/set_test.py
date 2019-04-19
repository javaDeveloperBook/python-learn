student={'tom','mark','jack','rose'}
print(student)

#成员测试
if 'rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
#set可以进行集合运算
a=set('abcd')
b=set('afhg')
print(a-b)
print(a|b)
print(a&b)
#a 与 b中不同时存在的元素
print(a^b)