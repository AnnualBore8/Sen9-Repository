# TODO решить с помощью list comprehension и распечатать его

import pprint

list_keys = ['bin', 'dec', 'hex', 'oct']
a = []
for i in range(16):
    bin_ = bin(i)
    dec_ = int(i)
    hex_ = hex(i)
    oct_ = oct(i)
    list_ = [bin_, dec_, hex_, oct_]
    dict_ = {k: v for k, v in zip(list_keys, list_)}
    a.append(dict_)

pprint.pprint(a)

