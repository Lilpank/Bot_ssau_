import requests
from bs4 import BeautifulSoup

url = 'https://ssau.ru/rasp?groupId=531874164&selectedWeek=2&selectedWeekday=1'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=header)

txt_response = response.text
soup = BeautifulSoup(txt_response, 'lxml')

block_data_lesson = soup.find_all('div', class_='schedule__item')

data = list()
for block in block_data_lesson:
    data.append(block.get_text())

day_of_week: list = []
day_of_week += [day for day in data[1:7]]
print(day_of_week)

weekly_schedule: dict = {}

Monday: list = []
Monday += [lesson for lesson in data[7:len(data):6]]
weekly_schedule[day_of_week[0]] = Monday

Tuesday: list = []
Tuesday += [lesson for lesson in data[8:len(data):6]]
weekly_schedule[day_of_week[1]] = Tuesday

Wednesday: list = []
Wednesday += [lesson for lesson in data[9:len(data):6]]
weekly_schedule[day_of_week[2]] = Wednesday

Thursday: list = []
Thursday += [lesson for lesson in data[10:len(data):6]]
weekly_schedule[day_of_week[3]] = Thursday

Friday: list = []
Friday += [lesson for lesson in data[11:len(data):6]]
weekly_schedule[day_of_week[4]] = Friday

Saturday: list = []
Saturday += [lesson for lesson in data[12:len(data):6]]
weekly_schedule[day_of_week[5]] = Saturday

print(weekly_schedule)
