salary,spend,months,increase  = 5000,6000,10,0.03
fin_pillow=[spend-salary]
cur_spend=spend

for mon in range(months-1):
    cur_spend*=(1+increase)
    fin_pillow.append(cur_spend - salary)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",round(sum(fin_pillow)) )
