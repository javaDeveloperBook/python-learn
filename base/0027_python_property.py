class Student:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise TypeError('score must be int.')
        if value < 0 or value > 100:
            raise ValueError('score is in 0-100.')
        self._score = value


stu = Student('jack', 100)
print(stu.score)
stu.score = '1212'
stu.score = 999
print(stu.score)


