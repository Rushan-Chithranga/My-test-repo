-- query to get all users who have not returned at least one book

SELECT users.id, users.first_name, users.last_name, users.email, users.registered_on
FROM lendings
RIGHT JOIN users ON lendings.user_id = users.id
WHERE lendings.date_due  < NOW()
GROUP BY users.id;