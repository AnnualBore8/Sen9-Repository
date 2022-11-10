from random import randint


def get_unique_list_numbers() -> list[int]:
    a = []
    while len(a) < 15:
        b = randint(-10, 10)
        if b not in a:
            a.append(b)
    return a

    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))