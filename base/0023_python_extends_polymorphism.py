class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(animal):
        animal.run()


class Duck(Animal):
    def run(self):
        print('Duck is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running... ')


Animal.run_twice(Dog())
Animal.run_twice(Duck())
