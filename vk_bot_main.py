import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token) # подключение токена
longpoll = VkBotLongPoll(vk_session, 205640140) # грубо говоря само подключение

# отправляем сообщения через id (в данном случае id группы)
def sender(id, text):
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

# проверка событий ...
for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW: # пришло новое сообщение? это наш клиент)
		if event.from_chat:
			id = event.chat_id
			msg = event.message.__str__
			
			if msg == 'ааа':
				sender(id, 'аааа!')
			