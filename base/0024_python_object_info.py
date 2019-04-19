# 判断对象类型，使用type()函数
import types

print(type(123))
print(type('asa'))
print(type(None))
print(type(True))


def fun():
    pass


print(type(fun) == types.FunctionType)


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

class Animal(object):
    def run(self):
        print('running...')


class Dog(Animal):
    def __init__(self, name):
        self.name = name


print(isinstance(Dog('dog'), Animal))


# 获得一个对象的所有属性和方法，可以使用dir()函数，
dog = Dog('Tom')
print(dir(dog))

if hasattr(dog, 'name'):
    setattr(dog, 'name', 'new name')
print(dog.name)
fn = getattr(dog, 'run')
fn()

