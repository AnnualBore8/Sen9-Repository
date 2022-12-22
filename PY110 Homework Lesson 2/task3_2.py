def int_check(fn):
    def wrapper(arg):
        if type(arg) != type(10):
            raise ValueError("Не все позиционные аргументы (*args) функции являются типом int")
        result = fn(arg)
        return result
    return wrapper


@int_check# TODO задекорировать функцию
def some_func(str_arg: int) -> int:
    print(str_arg)


if __name__ == "__main__":
    some_func(1)  # всё хорошо

    some_func("Short str")  # ValueError