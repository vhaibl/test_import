# -*- coding: utf-8 -*-

import simple_draw as sd
from picture.tree import tree
from picture.tree import tree2
from picture.sky import sun
# from picture.sky import sun2
from picture.sky import rainbow
from picture.house import house
from picture.redneck import smile
from picture.redneck import smile2
from picture.snowfall import snowfall

sd.resolution = (1200, 800)

sd.clear_screen()
counter = 0
r_counter = 0
while True:
    # Общий цикл и счетчик тоже надо в пакет засунуть?
    # TODO общий цикл нет, а вот счётчики можно попробовать
    counter += 1
    r_counter += 1
    sd.start_drawing()
    tree()
    tree2()
    house()
    sun(counter)
    smile(counter)
    snowfall()
    sd.finish_drawing()

    rainbow(r_counter)
    if r_counter >= 7:  # TODO Это можно хитро записать при помощи тернарного оператора
        # TODO счётчик = 0 if условие else счётчик + 1
        # TODO Это будет равносильно записи
        # if условие
        #     счётчик = 0
        # else
        #     счётчик = счётчик + 1
        r_counter = 0
    if counter > 100:
        counter = 0
# TODO А так - красота! :)
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()
