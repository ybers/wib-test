-- A
SELECT avg(i.price) FROM 'user' u
LEFT JOIN purchase p ON u.id = p.user_id
LEFT JOIN item i ON p.item_id = i.id
WHERE u.age BETWEEN 18 AND 25;
--
SELECT avg(i.price) FROM 'user' u
LEFT JOIN purchase p ON u.id = p.user_id
LEFT JOIN item i ON p.item_id = i.id
WHERE u.age BETWEEN 26 AND 35;

-- Б
SELECT strftime('%m', p.'date') as 'month', sum(i.price) as amount FROM purchase p
LEFT JOIN 'user' u ON  p.user_id = u.id
LEFT JOIN item i ON p.item_id = i.id
WHERE u.age > 35
GROUP BY month
ORDER BY amount DESC
LIMIT 1;

-- В
WITH cte AS (
SELECT strftime('%Y', p.'date') as 'year', item_id FROM purchase p
)
SELECT item_id, year, sum(i.price) as amount FROM cte
LEFT JOIN item i ON cte.item_id = i.id
WHERE year = (SELECT max(year) FROM cte)
GROUP BY item_id
ORDER BY amount DESC
LIMIT 1;

-- Г
WITH cte AS (
SELECT
i.id as 'item_id', sum(i.price) as 'revenue',
CAST(strftime('%Y', p.'date') as INT) as 'year'
FROM purchase p
LEFT JOIN item i ON p.item_id = i.id
WHERE year = 2018
GROUP BY item_id
ORDER BY revenue DESC
)
SELECT item_id, revenue,
CAST (revenue / (SELECT sum(revenue) * 1.0 FROM cte) as float) as relative_revenue
FROM cte
LIMIT 3;
