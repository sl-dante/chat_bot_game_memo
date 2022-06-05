import sqlite3

conn = sqlite3.connect("game_memo.db")
cursor = conn.cursor()


# Скрипт для создания базы данных
def create_table():
    cursor.execute('''
              CREATE TABLE IF NOT EXISTS Type_Chess(
              ID INTEGER PRIMARY KEY,
              NAME TEXT NOT NULL
              )''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Chess(
                ID INTEGER PRIMARY KEY,
                NAME TEXT NOT NULL,
                DESCRIPTION TEXT,
                PATH_PHOTO TEXT,
                TYPE INTEGER,
                FOREIGN KEY (TYPE) REFERENCES Type_Chess(ID)
                )''')


# Класс Шахматы для удобной записи в БД
class Chess:
    def __init__(self, _id, _name, _description, _path_photo, _type):
        self.id = _id,
        self.name = _name,
        self.description = _description
        self.path_photo = _path_photo
        self.type = _type


if __name__ == '__main__':
    create_table()
