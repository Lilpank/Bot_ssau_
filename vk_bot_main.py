import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token # создать config.py спеременной main_token='написать токен здесь'

vk_session = vk_api.VkApi(token = main_token) # подключение токена
longpoll = VkBotLongPoll(vk_session, 205640140) # грубо говоря само подключение


def get_user_name(self, user_id):
    """ Получаем имя пользователя"""
    return self.vk_api.users.get(user_id=user_id)[0]['first_name']


# отправляем сообщения через id (в данном случае id группы)
def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

# проверка событий ...
for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW: # пришло новое сообщение? это наш клиент)
		if event.from_chat:
			id = event.chat_id
			msg = event.obj['message']['text']
			# username = get_user_name(event.message.from_id) # не работает надо придумать как пофиксить
			if msg == '[club205640140|test_bot_ssau] help':
				sender(id, 'sometext')

'''
1)нужно добавить список команд
2)есть проблемы с тем чтобы получать id пользователя который сделал зопрос(можно и без этого)
3)не понятно насколько нормально отслеживать команды подобным образом [club205640140|test_bot_ssau] <название команды>
если есть другой способ нужно его рассматреть
4)переписать все по отдельным классам
5)пропистаь команды в enum class 
'''