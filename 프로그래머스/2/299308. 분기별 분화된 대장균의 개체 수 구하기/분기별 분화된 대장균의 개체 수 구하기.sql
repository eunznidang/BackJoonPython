SELECT 
    CONCAT(
        CASE 
            WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 1 AND 3 THEN '1'
            WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN '2'
            WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN '3'
            ELSE '4'
        END
        , 'Q'
    ) AS quarter,
    COUNT(*) AS ecoli_count
FROM ecoli_data
GROUP BY quarter
ORDER BY quarter;