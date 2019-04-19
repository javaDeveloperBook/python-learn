class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print(self.__name, ':', self.__score)

    def get_name(self):
        return self.__name


stu = Student('jack', 100)
stu.print_score()

stu.__name = 'new name'


# 实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，
# 而外部代码给bart新增了一个__name变量
print(stu.__name)
print(stu.get_name())
