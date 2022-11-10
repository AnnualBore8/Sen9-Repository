from random import sample, randint
import string


# # Первый вариант
# def get_random_password(n = 8) -> str:
#     s = 'abcdefghijklmnopqrstuvwxyz'
#     ss = s.upper()
#     num = '123456789'
#     random_var = str(s + ss + num)
#     return ''.join((sample(random_var, k=n)))

# ...  # TODO написать функцию генерации случайных паролей

# второй вариант
def get_random_password(n=8) -> str:
    down_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    num = '123456789'

    random_var = str(down_letters + upper_letters + num)
    return ''.join((sample(random_var, k=n)))


print(get_random_password())
print(get_random_password(15))
