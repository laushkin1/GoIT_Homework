SELECT g.name AS group_name, AVG(m.mark) AS average_mark
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
WHERE sub.name = ?
GROUP BY g.name;
