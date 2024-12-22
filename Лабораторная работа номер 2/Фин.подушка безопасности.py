money_capital, salary, spend, increase = 20000, 5000, 6000, 0.05

months = 0

cur_capital = money_capital

budget = cur_capital + salary

while True:
    if budget>=spend:
        months+=1
        budget+=salary-spend
        spend*=(1+increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:",months)
