SELECT s.name AS student_name, m.mark, m.date
FROM marks m
JOIN students s ON m.student_id = s.id
JOIN subjects sub ON m.subject_id = sub.id
WHERE s.group_id = ? AND sub.name = ?;
