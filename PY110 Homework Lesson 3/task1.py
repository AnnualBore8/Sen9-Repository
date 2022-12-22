import json
import random


def task():
    with open('new_file_1.json', 'w') as file_1, open('new_file_2.json', 'w') as file_2:

        rand_list_1 = list(map(lambda i: random.randint(-10, 10), range(15)))
        rand_list_2 = list(map(lambda i: random.randint(-10, 10), range(15)))
        # print(rand_list_1)
        # print(rand_list_2)

        return json.dump(rand_list_1, file_1, indent=4), json.dump(rand_list_2, file_2, indent=4)


def read():
    file_1 = 'new_file_1.json'
    file_2 = 'new_file_2.json'

    with open(file_1, 'r') as f_1_r, open(file_2, 'r') as f_2_r:
        a, b = json.load(f_1_r), json.load(f_2_r)
        return print(a, '\n', b)


if __name__ == "__main__":
    # Write your solution here
    task()
    read()
    pass
