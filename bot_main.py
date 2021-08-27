import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import my_parser
from bot_command import COMMAND_INPUT_URL, COMMAND_HELP, COMMAND_SCHEDULE, COMMAND_HELLO, BOT_NAME
import message_generator
from config import main_token

vk_session = vk_api.VkApi(token=main_token)  # подключение токена \ авторизация бота
longpoll = VkBotLongPoll(vk_session, 205640140)  # грубо говоря само подключение \ работа с сообщениями


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
                sender(id, message_generator.message_to_help())
            elif msg in COMMAND_HELLO:
                user_get = vk_session.get_api().users.get(user_ids=event.message.from_id)[0]
                sender(id, message_generator.message_to_hello(user_get['first_name']))
            # Если приходит сообщение url=https://ssau.ru/rasp?groupId=531874164&selectedWeek=2&selectedWeekday=1
            elif msg[:4] == COMMAND_INPUT_URL:
                try:
                    sender(id, my_parser.Parser(msg[4:]).get_weekly_schedule())
                except my_parser.Exception_day:
                    sender(id, 'Ошибка в расписании')
            elif msg == COMMAND_SCHEDULE:
                sender(id, 'Расписание на сегодня: ...')  # TODO: доделать вывод расписания.
            elif msg[0:len(BOT_NAME)] == BOT_NAME:
                sender(id, message_generator.message_error() + '\n' + message_generator.message_to_help())
