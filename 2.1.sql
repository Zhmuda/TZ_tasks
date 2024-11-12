SELECT 
    r.user_id,
    SUM(r.reward) AS total_reward_2022
FROM 
    reports r
WHERE 
    r.user_id IN (
        SELECT user_id
        FROM reports
        GROUP BY user_id
        HAVING MIN(created_at) >= '2021-01-01' 
           AND MIN(created_at) < '2022-01-01'
    )
    AND r.created_at >= '2022-01-01' 
    AND r.created_at < '2023-01-01'
GROUP BY 
    r.user_id;
