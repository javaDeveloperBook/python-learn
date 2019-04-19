def now():
    print('2019-04-18')


def wapper(func):
    print('wapper:',func.__name__)
    return func()


wapper(now)


