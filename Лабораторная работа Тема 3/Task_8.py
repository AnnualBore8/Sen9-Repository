money_capital: int = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

# while True:
#     if money_capital + salary < spend:
#         break
#     if month == 0:
#         money_capital = money_capital + salary - spend
#         print('Осталось денег в ', month + 1, 'месяц', money_capital)
#         month += 1
#         a = 1
#     elif month != 0:
#         a += increase
#         print(a)
#         # spend *= a
#         # print(spend)
#         money_capital = money_capital + salary - spend * a
#         if money_capital < 0:
#             break
#         print('Осталось денег в ', month + 1, 'месяц', money_capital)
#         month += 1

while True:

    if month == 0:
        money_capital = money_capital - spend + salary
        # print('Осталось денег в ', month + 1, 'месяц', money_capital)
        month += 1
        a = 1
    elif month != 0:
        a += increase
        # print('Ставка в месяце ', month +1, ' = ', a)
        spend *= a
        # print(spend)
        money_capital = money_capital - spend
        if money_capital < 0:
            break
        money_capital += salary
        # print('Осталось денег в ', month + 1, 'месяц', money_capital)
        month += 1

print(month)
