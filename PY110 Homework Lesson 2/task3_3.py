
# я не знаю, что делать
# вариант 1 - очень кривой
#
# from collections.abc import Iterable
#
#
# def print_args_kwargs(*args, **kwargs):
#
#     if isinstance(args, Iterable):
#         raise TypeError(f"Объект {args} {type(args)} не является итерируемым")
#
#     if isinstance(kwargs, Iterable):
#         raise TypeError(f"Объект {kwargs} {type(kwargs)} не является итерируемым")
#
#     return print(args, kwargs)


# if __name__ == "__main__":
    # print_args_kwargs([1,2,3,4,5], 'qwerty')
    # print_args_kwargs(1)


def is_itter(args, kwargs):
    # while True:
    try:
        iter(args)
        print(args, ' is good')
    except TypeError as te:
        print(args, ' is ', te)

    try:
        iter(kwargs)
        print(kwargs, ' is good')
    except TypeError as te:
        print(kwargs, ' is ', te)
    return

is_itter([1,2,3,4], 'ffffffff')
is_itter([1,2,3,4], 1)
is_itter(1.5, 1)




