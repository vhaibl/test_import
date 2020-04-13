# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

file_name = 'events.txt'


class Parser:
    def __init__(self, file_name):
        self.filtered = {}
        self.file_name = file_name

    def prepare(self):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                filter = line[1:17]
                self.create(filter, line)

    def create(self, filter, line):
        if 'NOK' in line:
            if filter in line:
                if filter in self.filtered:
                    self.filtered[filter] += 1
                else:
                    self.filtered[filter] = 1
            else:
                self.filtered = {filter: 1}

    def result(self):
        print('__________________MINUTE STATS___________________')

        for date, count in self.filtered.items():
            print(date, count)

    def run(self):
        self.prepare()
        self.result()


class Hours(Parser):
    def prepare(self):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                filter = line[1:14]
                self.create(filter, line)

    def result(self):
        print('__________________HOUR STATS___________________')
        for date, count in self.filtered.items():
            print(date, 'hour -', count)

class Month(Parser):
    def prepare(self):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                filter = line[1:8]
                self.create(filter, line)

    def result(self):
        print('__________________MONTH STATS___________________')
        for date, count in self.filtered.items():
            print(date[0:4], 'year', date[5:7], 'month - ', count)

class Year(Parser):
    def prepare(self):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                filter = line[1:8]
                self.create(filter, line)

    def result(self):
        print('__________________YEAR STATS___________________')
        for date, count in self.filtered.items():
            print(date[0:4], 'year - ', count)

parse = Parser(file_name='events.txt')
parse.run()

parse = Hours(file_name='events.txt')
parse.run()

parse = Month(file_name='events.txt')
parse.run()

parse = Year(file_name='events.txt')
parse.run()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
