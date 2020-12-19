import datetime
from utils import emotions, response
from data_base import insert_into_db


# функция бота - цикл сообщение пользователя/ответ бота
def chat_bot(host_address, port_address, username, user_password):
    last_emotion = None
    while True:
        last_emotion, bot_answer, text_time, user_text = get_answer(last_emotion)
        print(bot_answer)
        insert_into_db(text_time, user_text, bot_answer, host_address, port_address, username, user_password)


# получаем ответ бота
def get_answer(last_emotion):
    current_emotion, text_time, user_text = get_current()
    if last_emotion is None and current_emotion is not None:
        response_emotion = '{} greeting'.format(current_emotion)
    elif last_emotion is not None and current_emotion is not None:
        response_emotion = '{} {}'.format(last_emotion, current_emotion)
    else:
        response_emotion = 'not understood'
    return current_emotion, response[response_emotion], text_time, user_text


# получаем сообщение пользователя и интерпретируем его эмоциональный окрас ['happy', 'sad', 'angry']
def get_current():
    raw_input = input()
    text_time = datetime.datetime.now()
    user_text = raw_input
    emoji = raw_input.encode('utf-8')
    if emoji in emotions.keys():
        return emotions[emoji], text_time, user_text
    else:
        # пользователь может ввести и очень длинное сообщение, чтобы не создавать VARCHAR(i) с очень большим i
        # можно хранить 'TEXT', так как, кажется, не так важно, что именно пользователь ввел
        return None, text_time, 'TEXT'
