from bot_command import COMMAND_HELP, COMMAND_SCHEDULE, COMMAND_INPUT_URL, COMMAND_HELLO


def message_to_hello(name):
    return "Привет, " + name + '!'


def message_to_help():
    return 'Вот мои команды:' + str('\n' + COMMAND_HELP + '\n' + COMMAND_SCHEDULE + '\n' + COMMAND_INPUT_URL)


def message_error():
    return 'Такой команды не существует!'
