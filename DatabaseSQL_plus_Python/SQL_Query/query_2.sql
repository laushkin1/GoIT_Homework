SELECT s.name AS student_name, AVG(m.mark) AS average_mark
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
WHERE sub.name = ?
GROUP BY s.name
ORDER BY average_mark DESC
LIMIT 1;
