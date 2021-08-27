import vk_api.vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot.config import main_token  # создать config.py спеременной main_token='написать токен здесь'
from parser_url.parser import Parser
from bot.bot_command import COMMAND_INPUT_URL, COMMAND_HELP

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
            if msg == COMMAND_HELP:
                sender(id, 'sometext')
            # Если приходит сообщение url=https://ssau.ru/rasp?groupId=531874164&selectedWeek=2&selectedWeekday=1
            elif msg[:4] == COMMAND_INPUT_URL:
                sender(id, Parser(msg[4:]).get_weekly_schedule())
            else:
                sender(id, 'wtf')


