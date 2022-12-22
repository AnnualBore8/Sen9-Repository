# Мое решение согласно заданию
from itertools import pairwise


def my_task(c):
    for e in range(1):
        yield list(pairwise(c))


if __name__ == '__main__':
    a = my_task("ABCDEFG")
    print(next(a))
    pass


# Решение которое было изнчально
def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i + 1]


def task():
    for pair in pairwise("ABCDEFG"):
        print(pair)


if __name__ == "__main__":
    task()


