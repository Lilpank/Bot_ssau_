import vk_api.vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot.config import main_token  # создать config.py спеременной main_token='написать токен здесь'
from parser_url.parser import Parser
from bot.bot_command import COMMAND_INPUT_URL

vk_session = vk_api.VkApi(token=main_token)  # подключение токена \ авторизация бота
longpoll = VkBotLongPoll(vk_session, 205640140)  # грубо говоря само подключение \ работа с сообщениями


def get_user_name(self, user_id):
    """ Получаем имя пользователя"""
    return self.vk_api.users.get(user_id=user_id)[0]['first_name']


# отправляем сообщения через id (в данном случае id группы)
def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


# проверка событий ...
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:  # пришло новое сообщение? это наш клиент)
        if event.from_chat:
            id = event.chat_id
            msg = event.obj['message']['text']
            print("Пользователь написал - ", msg)
            # username = get_user_name(event.message.from_id) # не работает надо придумать как пофиксить
            if msg == '[club205640140|test_bot_ssau] help':
                sender(id, 'sometext')
            # Если приходит сообщение url=https://ssau.ru/rasp?groupId=531874164&selectedWeek=2&selectedWeekday=1
            elif msg[:4] == COMMAND_INPUT_URL:
                sender(id, Parser(msg[4:]).get_weekly_schedule())

'''
1)нужно добавить список команд
2)есть проблемы с тем чтобы получать id пользователя который сделал зопрос(можно и без этого)
3)не понятно насколько нормально отслеживать команды подобным образом [club205640140|test_bot_ssau] <название команды>
если есть другой способ нужно его рассматреть
4)переписать все по отдельным классам
5)пропистаь команды в enum class 
'''

"""
Мысли о проекте.
Я бы хотел, чтобы бот присылал расписание каждое утро на день. 
Нужно разобраться, как сохранить url в дальнейшем, чтобы парсер сам изменял url по истечении недели (изменялся только 
selectedWeek в запросе) и бот соответственно оповещал всех о расписании в начале дня.
Возможно нужно БД подкрутить.. не знаю.

Попробовать развернуть бота на каком либо сервере.

Следует обсудить как обрабатывать сообщения пользователя. Это основное, что на данный момент нужно сделать, 
к обработке сообщений необходимо подкрутить исключения.

При желании, придумать комманды боту. Можно, чтобы бот присылал картинку\гифку какую потребует пользователь, 
даже можно, чтобы на эту картинку через какой либо сервис вставлял мем на фон, такая маленька шалость.
Получается, конечно, солянка или франкенштейн, но это хороший опыт в программировании :D 

Мне не нравится как оформлен класс Parser в конструкторе какой-то кошмар, но и придумать другого пока не получилось, 
если сможешь подсказать, буду рад. 

"""
