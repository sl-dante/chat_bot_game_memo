from pathlib import Path

import vk_api
import urllib.request
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
import json
import const
import text_files
import keyboards

token = const.token

group_id = const.id_group
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
longPoll = VkBotLongPoll(vk_session, group_id=group_id)


# Кодирование клавиатуры в JSON-формат
def encode_keyboard_for_vk(keyboard):
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


def create_event_message(message, chat_bot_responce):
    if event.obj.text.lower() == message.lower():
        if event.from_user:
            vk.messages.send(
                user_id=event.obj.from_id,
                random_id=get_random_id(),
                message=chat_bot_responce)


for event in longPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text.lower() == 'начать' or event.obj.text.lower() == 'привет':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Здраствуй',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == 'правила игры':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Выберите шахматы для которых вы хотите изучить правила игры',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_choice_chess))



        if event.obj.text.lower() == 'тест':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Для вас будет проведен тест по знанию карточек, как будете готовы нажмите "Начать"')

        if event.obj.text.lower() == 'справка чат-бота':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Выберите категорию\n'
                            '1. Подробнее о правилах игры\n'
                            '2. Подробнее о выборе шахмат\n'
                            '3. Подробнее о тестировании\n')

            if event.obj.text.lower() == 'подробнее о правилах игры':
                if event.from_user:
                    vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message='Выберите категорию\n'
                                '1. Подробнее о правилах игры\n'
                                '2. Подробнее о выборе шахмат\n'
                                '3. Подробнее о тестировании\n')
