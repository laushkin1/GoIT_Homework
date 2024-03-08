SELECT s.name, AVG(m.mark) AS average_mark
FROM students s
JOIN marks m ON s.id = m.student_id
GROUP BY s.name
ORDER BY average_mark DESC
LIMIT 5;
