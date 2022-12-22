from itertools import pairwise


def get_distance(point) -> list:
    row = list(pairwise(point))
    a = []
    for i in row:
        len_ = ((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5
        a.append(len_)
    return a


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]


def hh(s):
    return print(sum(get_distance(s)))
hh(pts)

# # проработка решения
# print(list(pairwise(pts)))
# a = (list(pairwise(pts)))
# b = 0
# for i in a:
#     print(i)
#     print(((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5)
#     b += (((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5)
# print(b)