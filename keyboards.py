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
        [get_button('Вернуться в главное меню')],
    ]
}

# Клавиатура для изучения китайских шахмат
keyboard_for_china_chess = {
    'one_time': False,
    'buttons': [
        [get_button(label='Черный советник'),
         get_button(label='Красный советник'),
         get_button(label='Черная пушка')],
        [get_button(label='Красная пушка'),
         get_button(label='Черная ладья'),
         get_button(label='Красная ладья')],
        [get_button(label='Черный слон'),
         get_button(label='Красный слон'),
         get_button(label='Черный король')],
        [get_button(label='Красный король'),
         get_button(label='Черный конь'),
         get_button(label='Красный конь')],
        [get_button(label='Черная пешка'),
         get_button(label='Красная пешка'), ],
        [get_button('Вернуться в главное меню')],
    ]
}

# Клавиатура для изучения японских шахмат
keyboard_for_japan_chess = {
    'one_time': False,
    'buttons': [
        [get_button(label='Слон'),
         get_button(label='Перевёрнутый Слон'),
         get_button(label='Золото')],
        [get_button(label='Первый король'),
         get_button(label='Второй король'),
         get_button(label='Конь')],
        [get_button(label='Перевёрнутый Конь'),
         get_button(label='Пешка'),
         get_button(label='Перевёрнутая Пешка')],
        [get_button(label='Ладья'),
         get_button(label='Перевёрнутая Ладья'),
         get_button(label='Серебро')],
        [get_button(label='Перевёрнутое серебро'),
         get_button(label='Стрелка'),
         get_button(label='Перевёрнутая стрелка')],
        [get_button('Вернуться в главное меню')],
    ]
}
