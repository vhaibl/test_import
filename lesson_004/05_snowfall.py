# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
import simple_draw as sd

N = 20

x_list = []
y_list = []
size_list = []  # инициализация списков
new_list = []
for list_create in range(N + 1):
    x_list.append(sd.random_number(10, 600))
    y_list.append(sd.random_number(600, 1200))  # создание рандомных координат и размеров
    size_list.append(sd.random_number(10, 50))  # для N снежинок

while True:
    sd.start_drawing()
    for i, y in enumerate(y_list):
        # print(i, y, x_list[i])

        if y_list[i] >= 30:
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.background_color)
            y_list[i] -= sd.random_number(-5, 20)
            x_list[i] += sd.random_number(-15, 15)
            point = sd.get_point(x_list[i], y_list[i])
            # print(i, y_list[i])
            sd.snowflake(center=point, length=size_list[i], color=sd.COLOR_WHITE)
        else:
            fallen = []
            fallen = i, y_list[i], x_list[i]
            new_list.append(fallen)
            print("добавлена упавшая снежинка в список", new_list)

            y_list[i] += sd.random_number(600, 1200)
            sd.user_want_exit()
            break
        # TODO Попробуйте реализовать следующую идею:
        # TODO Снежинки, которые дошли до границы - записывайте по индексам в отдельный список
        # TODO Дальше, после этого цикла, пройдитесь циклом по списку с индексами и удаляйте упавшие снежинки
        # TODO Только удаляйте не с начала, а с конца (иначе индексы перепутаются)
    sd.sleep(0.02)
    sd.finish_drawing()
    for i, y, x in new_list:

        if y <= 30:
            point1 = sd.get_point(x, y)
            sd.snowflake(center=point1, length=size_list[i], color=sd.background_color)
            new_list.pop()  # TODO Я не совсем понял что нужно сделать, в цикле выше добавляю снежинки в список
                            # TODO В этом их удаляю, но они же там не задерживаются надолго...

        print("упавшие снежинки удалены", new_list)

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
