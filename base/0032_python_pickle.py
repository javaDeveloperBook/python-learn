import pickle

dic = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
file = open('test.pickle', 'wb')
pickle.dump(dic, file)
file.close()

with open('test.pickle', 'rb') as file1:
    res = pickle.load(file1)
    print(res)
