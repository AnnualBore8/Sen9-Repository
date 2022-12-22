if __name__ == "__main__":
    # Write your solution here
    def enum_to_zip(row):
        number = list(range(len(row)))
        for number, row in zip(number, row):
            print((number, row))
    pass


# Проверка правильности решения
# a = ['a', 'b', 'c', 'd']
# enum_to_zip(a)

# Анализ для вывода решения
# for i in enumerate(a):
#     print(i)
#
# numbers = list(range(len(a)))
#
# for a, numbers in zip(a, numbers):
#     print((numbers, a))
