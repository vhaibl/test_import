# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
i = 0
z = 1  # TODO Нэйминг стоит подправить. Если другим переменным сложно придумать полезное имя, то здесь подошел бы
# TODO Какой-нибудь count. Старайтесь сразу привыкать тратить часть времени на придумывание хороших имён, это поможет.
while i <= a:
    z += 1
    i = b * z
print("Целочисленное деление", a, "на", b, "дает", z - 1)
