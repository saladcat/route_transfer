class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2


def change(a):
    a.a = -1


if __name__ == '__main__':
    dic = {}
    a = A()
    change(a)

    print(a.a)
