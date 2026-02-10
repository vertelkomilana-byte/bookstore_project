import sqlite3

# подключаемся к базе
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# создаём таблицы
cursor.executescript("""
CREATE TABLE IF NOT EXISTS author (
    author_id INTEGER PRIMARY KEY,
    name_author TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS genre (
    genre_id INTEGER PRIMARY KEY,
    name_genre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    genre_id INTEGER,
    price REAL,
    amount INTEGER,
    FOREIGN KEY (author_id) REFERENCES author(author_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);
""")

# заполняем таблицы
cursor.executescript("""
INSERT INTO genre VALUES
(1, 'Роман'),
(2, 'Поэзия'),
(3, 'Приключения');

INSERT INTO author VALUES
(1, 'Булгаков М.А.'),
(2, 'Достоевский Ф.М.'),
(3, 'Есенин С.А.'),
(4, 'Пастернак Б.Л.'),
(5, 'Лермонтов М.Ю.');

INSERT INTO book VALUES
(1, 'Мастер и Маргарита', 1, 1, 670.99, 3),
(2, 'Белая гвардия', 1, 1, 540.50, 5),
(3, 'Братья Карамазовы', 2, 1, 799.01, 3),
(4, 'Игрок', 2, 1, 480.50, 10),
(5, 'Стихотворения и поэмы', 3, 2, 650.00, 15),
(6, 'Черный человек', 3, 2, 570.20, 6),
(7, 'Лирика', 4, 2, 518.99, 10),
(8, 'Идиот', 2, 1, 460.00, 10),
(9, 'Герой нашего времени', 5, 3, 570.59, 2),
(10, 'Доктор Живаго', 4, 3, 740.50, 5);
""")

# сохраняем изменения и закрываем базу
conn.commit()
conn.close()

print("База данных создана и заполнена")
