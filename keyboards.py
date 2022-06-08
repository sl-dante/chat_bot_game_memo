# ----------------------------------------------------------
# Файл, где находятся все клавиатуры используемые в чат-боте
# ----------------------------------------------------------

import json


# Функция для создания кнопки
def get_button(label, color='primary', payload=''):
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
        [get_button(label='Правила игры')],
        [get_button(label='Обучение')],
        [get_button(label='Тест')],
        [get_button(label='Справка чат-бота')],
    ]
}

# Клавиатура при объяснении правил
keyboard_for_rules = {
    'one_time': False,
    'buttons': [
        [get_button('Выбрать другой тип шахмат')],
        [get_button('Вернуться в главное меню')]
    ]
}

# Клавиатура для обучения
keyboard_for_education = {
    'one_time': False,
    'buttons': [
        [get_button('Вернуться в главное меню')]
    ]
}
# Клавиатура выбора шахмат
keyboard_for_choice_chess = {
    'one_time': False,
    'buttons': [
        [get_button(label='Японские шахматы')],
        [get_button(label='Китайские шахматы')],
        [get_button(label='Вернуться в главное меню')],

    ]
}

# Клавиатура для тестирования
keyboard_for_testing = {
    'one_time': False,
    'buttons': [
        [get_button(label='Начать тестирование', color='primary')],
        [get_button(label='Вернуться в главное меню')],
    ]
}

# Клавиатура для справки
keyboard_for_FAQ = {
    'one_time': False,
    'buttons': [
        [get_button(label='Подробнее о правилах игры')],
        [get_button(label='Подробнее о выборе шахмат')],
        [get_button(label='Подробнее о тестировании')],
        [get_button(label='Подробнее об обучении')],
        [get_button(label='Вернуться в главное меню')],
    ]
}

# Клавиатура для выбора числа вопросов
keyboard_for_choice_count = {
    'one_time': False,
    'buttons': [
        [get_button(i) for i in range(4, 8)],
        [get_button(i) for i in range(8, 12)],
        [get_button(i) for i in range(12, 16)],
    ]
}
