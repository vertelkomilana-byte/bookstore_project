SELECT title, amount
FROM book
WHERE amount < 5;

SELECT g.name_genre, SUM(b.amount) AS total_amount
FROM book b
JOIN genre g ON b.genre_id = g.genre_id
GROUP BY g.genre_id;