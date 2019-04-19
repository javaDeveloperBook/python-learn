L = ['jack', 'Tom', 'Mike','jack', 'Tom', 'Mike']
print(L[2:5])

nums = list(range(100))
# 后10个数
print('后10个数:', nums[-10:])
print('前10个数:', nums[:10])
print('前10个数，每两个取一个:', nums[:10:2])
print('所有数，每5个取一个:', nums[::5])

nums1 = tuple(range(100))
print('tuple 所有数，每5个取一个:',nums1[::5])

print('字符串切片：', 'ABCDEFG'[2:5])