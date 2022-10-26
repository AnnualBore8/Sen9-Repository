list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]
set_ = set(list_)

# предположим, что первый элемент в нашем списке минимальный
min_value_index = 0
min_value = list_[min_value_index]


# TODO заменить на enumerate
# for i in range(len(list_)):
#     current_value = list_[i]
#     if current_value <= min_value:
#         min_value = current_value
#         min_value_index = i

for index, value in enumerate(list_): # Правильное решение

    if value <= min_value: # Правильное решение
        min_value = value # Правильное решение
        min_value_index = index # Правильное решение

print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
