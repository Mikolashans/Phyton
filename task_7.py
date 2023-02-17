print('Задача 7. Режем число на части')
number = int(input('Введите четырехзначное число: '))
number4 = number % 10
number3 = number % 100 // 10
number2 = (number % 1000 //100)
number1 = number // 1000
print('Первая цифра: ', number1)
print('Вторая цифра: ', number2)
print('Третья цифра: ', number3)
print('Четвертая цифра: ', number4)