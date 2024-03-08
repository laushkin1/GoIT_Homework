SELECT t.name AS teacher_name, AVG(m.mark) AS average_mark
FROM teachers t
JOIN subjects sub ON t.id = sub.teacher_id
JOIN marks m ON sub.id = m.subject_id
WHERE t.id = ?
GROUP BY t.name;
