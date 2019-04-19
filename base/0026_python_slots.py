class Student(object):
    __slots__ = ('name', ' age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


# TypeError: __slots__ must be identifiers
stu = Student('jack', 10)
stu.score = 100


