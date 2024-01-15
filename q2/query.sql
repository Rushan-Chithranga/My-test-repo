-- query to get all users who have not returned at least one book

SELECT users.user_id users.first_name, users.last_name, users.email, users.registered_at, lendings.id
FROM lendings
RIGHT JOIN users ON lendings.user_id = users.user_id
WHERE lendings.due_data < NOW()
GROUP BY users.user_id;