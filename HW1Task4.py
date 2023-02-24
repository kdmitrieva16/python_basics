revenue = int(input("Введите выручку фирмы"))
costs = int(input("Введите издержки фирмы"))
if revenue > costs:
    profit = revenue - costs
    print(f'Финансовый результат - прибыль. Ее величина: {profit}')
    rent = profit / revenue
    print(f'Рентабельность выручки = {rent}')
    count_of_employer = int(input("Введите численность сотрудников фирмы"))
    profit_for_employer = profit / count_of_employer
    print(
        f'Прибыль фирмы в расчете на одного сотрудника = {profit_for_employer}')
else:
    print(
        f'Финансовый результат - убыток. Его величина: {costs - revenue}')