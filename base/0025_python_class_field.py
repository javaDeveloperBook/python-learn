class Student(object):
    name = None

    def __init__(self, age, score):
        self.age = age
        self.score = score


stu1 = Student(11, 100)
stu1.name = 'Jack'

stu2 = Student(20, 99)

print(stu1.name)
print(stu2.name)

