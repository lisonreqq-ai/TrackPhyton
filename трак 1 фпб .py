money_capital = 20000  # Подушка безопасности
salary = 5000          # Ежемесячная зарплата
spend = 6000           # Траты за первый месяц
increase = 0.05        # Ежемесячный рост цен

months = 0

while True:
    money_capital += salary

    if money_capital < spend:
        break

    money_capital -= spend
    months += 1
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", months)


