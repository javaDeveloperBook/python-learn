# list是一种有序的集合
students = ['Jack', 'Tom', 'hha']
print(students)

# len()函数可以获得list元素的个数
print(len(students))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始
print(students[1])
print(students[-1])

langugelist = ['java', 'python', ['c', 'go']]
print(langugelist)


# 有序列表叫元组：tuple，tuple和list非常类似，但是tuple一旦初始化就不能修改，比 list 更加安全
classmates = ('Jack', 'Tom', 'Mike')
print(classmates)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
one = (1)
one_tuple = (1,)
print(one)
print(one_tuple)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
# 如指向的是一个 list 则不能再指向其他对象了，但是指向的这个 list 本身是可变的
tuple_list = ('Jack', 'python', ['c','go'])
print(tuple_list)
tuple_list[2][0] = 'c++'
print(tuple_list)
