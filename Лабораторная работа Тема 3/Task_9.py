salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

months_start = 1
need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
# while True:
#     if months_start > 1:

spend_first_months = spend
a = 1 + increase
for i in range(1,10):
    spend *= round(a, 2)
    need_money += spend
    # print("Нужно денег в ", need_money)

have_money = 0
for f in range(1, 11):
    have_money = salary * f
    # print("Есть деньги в ", f, ' месяц ',have_money)

need_money = need_money + spend_first_months - have_money
print(round(need_money))
