from itertools import count


def generator():

    base = int(input('Введите первый член: '))
    step = int(input('Введите знаменатель прогрессии: '))

    num = base
    yield num

    for i in count(1, 1):
        yield base * step ** i


if __name__ == "__main__":
    numbers = generator()

    for k in range(11):
        print(next(numbers))
    # Write your solution here
    pass
