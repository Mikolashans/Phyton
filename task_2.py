print('Задача 2. Финансовый отчёт')
profit1qa = int(input('Введите прибыль за 1-й квартал: ')) 
profit2qa = int(input('Введите прибыль за 2-й квартал: ')) 
profit3qa = int(input('Введите прибыль за 3-й квартал: ')) 
profit4qa = int(input('Введите прибыль за 4-й квартал: ')) 
dinamics = (profit1qa + profit2qa) / (profit3qa + profit4qa)
print('Динамика роста: ', dinamics)