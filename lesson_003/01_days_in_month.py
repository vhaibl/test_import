# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
# long = (1,3,5,7,8,10,12)
# short = (4,6,9,11)
# feb = 2
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("В этом месяце 31 день")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("В этом месяце 30 дней")
elif month == 2:
    print("В этом месяце 28 дней")
else:
    print('Неправильный номер месяца')

# Что-то я не понял, как сравнить месяц со значением из списка(  хотел сделать типа if month == long:
# print ("31 день")
# TODO Догадка верная, вам нужен оператор 'in' - if элемент in список...
