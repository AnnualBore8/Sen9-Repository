list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

average = sum(list_numbers) / len(list_numbers)
list_numbers.insert(4, average)
list_numbers.pop(5)
print(list_numbers)

# более быстрое решение
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_numbers[4] = sum(list_numbers) / len(list_numbers)
print(list_numbers)