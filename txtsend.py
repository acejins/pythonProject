import sys


def printsave(*a):
    file = open('x.txt', 'a')

    print(*a)
    print(*a, file=file)

    file.close()


if __name__ == '__main__':
    printsave('PyCharm')
