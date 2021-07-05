import requests
from bs4 import BeautifulSoup
from parser_url.settings_parser import HEADER

"""
url = 'https://ssau.ru/rasp?groupId=531874164&selectedWeek=2&selectedWeekday=1'
Класс предназанчен для парсинга данных из url, в данном случае он содержит расписание на сегодняшний день.
для создания объекта требуется url адрес.
"""


class Parser:
    def __init__(self, url: str):
        self.url = url
        # Этот запрос возвращает объект Response
        response = requests.get(self.url, headers=HEADER)
        # достаем html разметку
        txt_response = response.text
        # Производим обертку, для использования метода find_all
        soup = BeautifulSoup(txt_response, 'lxml')
        # получаем нам нужны данные из таблицы.
        block_data_lesson = soup.find_all('div', class_='schedule__item')
        # в листе data все нужные данные, теперь нужно их достать.
        data = list()
        for block in block_data_lesson:
            data.append(block.get_text())
        # day_of_week содержит дни недели из таблицы, в дальнейшем это будет ключом dict
        self.day_of_week: list = []
        self.day_of_week += [day for day in data[1:7]]

        # структура у weekly_schedule = { 'day': 'schedule'}
        self.weekly_schedule: dict = {}
        # т.к ячейки таблицы располагаются слева на право, то можно их распарсить срезами списка таким образом:
        Monday: list = []
        Monday += [lesson for lesson in data[7:len(data):6]]
        self.weekly_schedule[self.day_of_week[0]] = Monday

        Tuesday: list = []
        Tuesday += [lesson for lesson in data[8:len(data):6]]
        self.weekly_schedule[self.day_of_week[1]] = Tuesday

        Wednesday: list = []
        Wednesday += [lesson for lesson in data[9:len(data):6]]
        self.weekly_schedule[self.day_of_week[2]] = Wednesday

        Thursday: list = []
        Thursday += [lesson for lesson in data[10:len(data):6]]
        self.weekly_schedule[self.day_of_week[3]] = Thursday

        Friday: list = []
        Friday += [lesson for lesson in data[11:len(data):6]]
        self.weekly_schedule[self.day_of_week[4]] = Friday

        Saturday: list = []
        Saturday += [lesson for lesson in data[12:len(data):6]]
        self.weekly_schedule[self.day_of_week[5]] = Saturday

    def get_weekly_schedule(self) -> str:  # метод возвращающий боту нужную информацию.
        schledule = str()
        # for key, value in self.weekly_schedule.items():
        #     schledule += value
        return schledule
