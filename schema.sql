CREATE TABLE author (
	author_id INTEGER PRIMARY KEY,
    name_author TEXT NOT NULL);

CREATE TABLE genre(
	genre_id INTEGER PRIMARY KEY,
    name_genre TEXT NOT NULL);

CREATE TABLE book (
	book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    aurhor_id INTEGER,
    genre_id INTEGER,
    price REAL,
    amount INTEGER,
    FOREIGN KEY (author_id) REFERENCES author(author_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);