# ----------------------------------------------------------
# Инициализация интерфейса
# ----------------------------------------------------------


from pathlib import Path
import vk_api
import urllib.request
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
import json
import const
import keyboards
import test
from common_method_for_project import *

token = const.token
group_id = const.id_group
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk_session)
longPoll = VkBotLongPoll(vk_session, group_id=group_id)

flag_for_education = False
flag_for_china_chess = False
flag_for_japan_chess = False


# Кодирование клавиатуры в JSON-формат
def encode_keyboard_for_vk(keyboard):
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    return keyboard


# Создание простого ответа чат-бота на сообщение пользователя
def create_event_message(message, chat_bot_responce, keyboard):
    if event.obj.text.lower() == message.lower():
        if event.from_user:
            vk.messages.send(
                user_id=event.obj.from_id,
                random_id=get_random_id(),
                message=chat_bot_responce,
                keyboard=keyboard)


# Создание ответа чат-бота с отправкой текста из текстового файла
def create_event_message_for_send_text(message, _path_text_file, keyboard):
    _absolute_path_for_root_directory = Path(__file__).resolve().parents[0]
    _absolute_path_for_text_file = f'{_absolute_path_for_root_directory}/text_files/' + _path_text_file
    _file_read = open(_absolute_path_for_text_file, 'r', encoding='UTF-8')

    return create_event_message(message, _file_read.read(), keyboard)


# Получение информации о шахматах при обучении
def get_chess_inform_from_event(name):
    if _event.obj.text.lower() == name.lower():
        if _event.from_user:
            _chess = select_chess_by_name(name.capitalize())

            if str(_chess.type) == '1':
                _keyboard = keyboards.keyboard_for_japan_chess
            elif str(_chess.type) == '2':
                _keyboard = keyboards.keyboard_for_china_chess
            else:
                _keyboard = keyboards.keyboard_for_start

            vk.messages.send(
                user_id=_event.obj.from_id,
                random_id=get_random_id(),
                message=f'Название: {_chess.name[0]}\n'
                        f'Описание: {_chess.description}\n'
                        'Если хотите выйти из изучения фигур, нажмите "Вернуться в главное меня"',
                keyboard=encode_keyboard_for_vk(_keyboard),
                attachment=load_photo(_chess, upload=upload))


# Основной цикл работы чат-бота
for event in longPoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text.lower() == 'начать' or event.obj.text.lower() == 'привет':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Здраствуй',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        create_event_message(
            message='правила игры',
            chat_bot_responce='Выберите шахматы для которых вы хотите изучить правила игры',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_choice_chess))

        create_event_message(
            message='тест',
            chat_bot_responce='Для вас будет проведен тест по знанию карточек, '
                              'как будете готовы нажмите "Начать"',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_rules))

        create_event_message(
            message='справка чат-бота',
            chat_bot_responce='Выберите категорию\n'
                              '1. Подробнее о правилах игры\n'
                              '2. Подробнее о выборе шахмат\n'
                              '3. Подробнее о тестировании\n'
                              '4. Подробнее об обучении\n',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_FAQ))

        create_event_message(
            message='подробнее о правилах игры',
            chat_bot_responce='При нажатии на эту клавишу, вам объяснят правила игры выбранных вами '
                              'шахмат, в данном проекте используются шахматы двух типов:\n'
                              '1. Китайские\n'
                              '2. Японские\n',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_FAQ))

        create_event_message(
            message='подробнее о выборе шахмат',
            chat_bot_responce='Перед тем, как узнать правила игры, пройти обучение или пройти тестирование'
                              'вам будет предложено выбрать вид шахмат, для которых будут описаны правила, '
                              'проведено тестирование или обучение',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_FAQ))

        create_event_message(
            message='подробнее о тестировании',
            chat_bot_responce='Тестирование подразумевает под собой, мини-игру, где вам показывают картинку '
                              'и предлагают выбрать один из нескольких вариантов ответов как, '
                              'называется фигура в виде кнопок, чтобы '
                              'получить бал, нужно ответить правильно',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_FAQ))

        create_event_message(
            message='подробнее об обучении',
            chat_bot_responce='Обучение подразумевает под собой, мини игру где вам предлагают клавиатуру на которой '
                              'отображены все фигуры, при нажатии на любую фигуру вам покажут картинку с этой фигурой '
                              'описание этой фигуры и то как она ходит',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_FAQ))

        create_event_message(
            message='вернуться в главное меню',
            chat_bot_responce='Ок',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        create_event_message(
            message='выбрать другой тип шахмат',
            chat_bot_responce='Выбирай',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_choice_chess))

        create_event_message(
            message='начать тестирование',
            chat_bot_responce='Введи количество карточек, которых ты получишь для тестирования',
            keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_choice_count))

        if event.obj.text.lower() == '4':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '5':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '6':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '7':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '8':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '9':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '10':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '11':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '12':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '13':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '14':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == '15':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Хорошо, тогда начинаем :)',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == 'китайские шахматы' and flag_for_education is False:
            if event.from_user:
                path_text_file = 'rules_for_china_chess.txt'
                absolute_path_for_root_directory = Path(__file__).resolve().parents[0]
                absolute_path_for_text_file = f'{absolute_path_for_root_directory}/text_files/' + path_text_file
                file_read = open(absolute_path_for_text_file, 'r', encoding='UTF-8')

                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=file_read.read(),
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))

        if event.obj.text.lower() == 'японские шахматы' and flag_for_education is False:
            if event.from_user:
                path_text_file = 'rules_for_japan_chess.txt'
                absolute_path_for_root_directory = Path(__file__).resolve().parents[0]
                absolute_path_for_text_file = f'{absolute_path_for_root_directory}/text_files/' + path_text_file
                file_read = open(absolute_path_for_text_file, 'r', encoding='UTF-8')

                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=file_read.read(),
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_rules))

        if event.obj.text.lower() == 'обучение':
            flag_for_education = True
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Выбери шахматы которые вы хотите изучить',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_choice_chess))

        if event.obj.text.lower() == 'китайские шахматы' and flag_for_education is True:
            flag_for_education = False
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Выбери фигуру которую вы хотите изучить',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_china_chess))

            for _event in longPoll.listen():
                if _event.type == VkBotEventType.MESSAGE_NEW:
                    get_chess_inform_from_event('Черный советник')

                    get_chess_inform_from_event('Красный советник')

                    get_chess_inform_from_event('Черная пушка')

                    get_chess_inform_from_event('Красная пушка')

                    get_chess_inform_from_event('Черный слон')

                    get_chess_inform_from_event('Красный слон')

                    get_chess_inform_from_event('Черная ладья')

                    get_chess_inform_from_event('Красная ладья')

                    get_chess_inform_from_event('Черный король')

                    get_chess_inform_from_event('Красный король')

                    get_chess_inform_from_event('Черная пешка')

                    get_chess_inform_from_event('Красная пешка')

                    get_chess_inform_from_event('Черный конь')

                    get_chess_inform_from_event('Красный конь')

                    if _event.obj.text.lower() == 'вернуться в главное меню':
                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message='Хорошо',
                                keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))
                            break

        if event.obj.text.lower() == 'японские шахматы' and flag_for_education is True:
            flag_for_education = False
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Выбери фигуру которую вы хотите изучить',
                    keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_japan_chess))

            for _event in longPoll.listen():
                if _event.type == VkBotEventType.MESSAGE_NEW:
                    get_chess_inform_from_event('Слон')

                    get_chess_inform_from_event('Перевёрнутый слон')

                    get_chess_inform_from_event('Золото')

                    get_chess_inform_from_event('Первый король')

                    get_chess_inform_from_event('Второй король')

                    get_chess_inform_from_event('Конь')

                    get_chess_inform_from_event('Перевёрнутый конь')

                    get_chess_inform_from_event('Пешка')

                    get_chess_inform_from_event('Перевёрнутая пешка')

                    get_chess_inform_from_event('Ладья')

                    get_chess_inform_from_event('Перевёрнутая ладья')

                    get_chess_inform_from_event('Серебро')

                    get_chess_inform_from_event('Перевёрнутое серебро')

                    get_chess_inform_from_event('Стрелка')

                    get_chess_inform_from_event('Перевёрнутая стрелка')

                    if _event.obj.text.lower() == 'вернуться в главное меню':
                        if _event.from_user:
                            vk.messages.send(
                                user_id=_event.obj.from_id,
                                random_id=get_random_id(),
                                message='Хорошо',
                                keyboard=encode_keyboard_for_vk(keyboards.keyboard_for_start))
                            break
