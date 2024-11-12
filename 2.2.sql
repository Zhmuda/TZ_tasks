SELECT 
    r.barcode,
    r.price
FROM 
    reports r
JOIN 
    pos p ON r.pos_id = p.id
GROUP BY 
    p.title, r.barcode, r.price
HAVING 
    COUNT(p.title) > 1;
