# dict的key必须是不可变对象
# 键-值（key-value）存储
score = {'Jack': 100, 'Tom': 88}
print(score['Jack'])

# 避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Jack' in score)

# get()方法，如果key不存在，可以返回None
print(score.get('Jack2'))

# 删除一个key，用pop(key)方法
print(score)
score.pop('Tom')
print(score)


# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set(['Jack', 'Tom', 'Mike'])
s1 = set(['Jack', 'Tom'])
print(s)
s.add('Jack')
print(s)
# s.remove('Jack')
# print(s)

print('交集:', s & s1)
print('并集:', s | s1)

# 不可变对象 ， 报错
t1 = tuple(1, 2, 3)
t2 = tuple(1, 2, [3, 4])
ts1 = set(t1)
print(ts1)

ts2 = set(t2)
print(ts2)


