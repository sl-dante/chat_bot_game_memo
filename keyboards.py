# ----------------------------------------------------------
# Файл, где находятся все клавиатуры используемые в чат-боте
# ----------------------------------------------------------

import json


# Функция для создания кнопки
def get_button(label, color, payload=''):
    return {
        'action': {
            'type': 'text',
            'payload': json.dumps(payload),
            'label': label
        },
        'color': color
    }


# Начальная клавиатура чат-бота
keyboard_for_start = {
    'one_time': False,
    'buttons': [
        [get_button(label='Правила игры', color='primary')],
        [get_button(label='Обучение', color='primary')],
        [get_button(label='Тест', color='primary')],
        [get_button(label='Справка чат-бота', color='primary')],
    ]
}

# Клавиатура при объяснении правил
keyboard_for_rules = {
    'one_time': False,
    'buttons': [

    ]
}

# Клавиатура для обучения
keyboard_for_education = {
    'one_time': False,
    'buttons': [

    ]
}
# Клавиатура выбора шахмат
keyboard_for_choice_chess = {
    'one_time': False,
    'buttons': [
        [get_button(label='Японские шахматы', color='primary')],
        [get_button(label='Китайские шахматы', color='primary')],
    ]
}

# Клавиатура для тестирования
keyboard_for_testing = {
    'one_time': False,
    'buttons': [
        [get_button(label='Начать тестирование', color='primary')],
    ]
}

# Клавиатура для справки
keyboard_for_FAQ = {
    'one_time': False,
    'buttons': [

    ]
}
