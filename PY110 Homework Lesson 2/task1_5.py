from string import ascii_lowercase, ascii_uppercase, digits
import random
from itertools import count


def password_generator(pass_, len_ = 8):
    for i in count(1, 1):
        yield ''.join(random.sample(pass_, len_))


if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    password = password_generator(ascii_lowercase + ascii_uppercase + digits, 16)
    for _ in range(11):
        print(next(password))

