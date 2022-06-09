import urllib
from pathlib import Path
import sqlite3
from creator_db import Chess

conn = sqlite3.connect("game_memo.db")
cursor = conn.cursor()


# Загрузка фотографий в вк
def load_photo(chess, upload):
    _type = ''
    if str(chess.type) == '1':
        _type = 'japan'
    elif str(chess.type) == '2':
        _type = 'china'
    absolute_path = Path(__file__).resolve().parents[0]
    path = f"{absolute_path}\\assets\\img_for_project\\{_type}_chess\\{chess.path_photo}"
    photo = upload.photo_messages(path)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    return attachment


# Запрос к БД для выбора шахмат по имени
def select_chess_by_name(name):
    cursor.execute(
        "SELECT * FROM Chess WHERE Name = ?", (str(name),))

    result = cursor.fetchall()
    result = result[0]
    _chess = Chess(_id=result[0],
                   _name=result[1],
                   _description=result[2],
                   _path_photo=result[3],
                   _type=result[4])

    return _chess
