'''
Данная вложенная проверяет, что результатом выполенния функций return_list и
return_tuple должен быть список (list). Если данное условие не соблюдается,
то программа выдает ошибку.
'''

def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        if not isinstance(result, list):
            raise TypeError(f"Результатом выполнения функции {fn} должен быть список")

    return wrapper


@output_type_list
def return_list() -> list:
    # print("Получилось")
    return []


@output_type_list
def return_tuple() -> str:
    # print("Не получилось")
    return ""


if __name__ == "__main__":
    return_list()
    return_tuple()
