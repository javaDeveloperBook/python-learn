list = ['jack', 'tom', 'mike', 'chen']
for v in list:
    print(v)

dic = {'1':'a', '2':'b', '3':'c'}

for k in dic:
    print(dic[k])

for v in dic.values():
    print(v)

for k, v in dic.items():
    print(k + ':' + v)


# print('判断是否可以迭代：', isinstance(dic, Iterable))


for i, v in enumerate(['A', 'B', 'C']):
    print(i, '=', v)
