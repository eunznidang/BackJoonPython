# select id
# , email
# , first_name
# , last_name

# from developers as d
# join (
# select * from skillcodes
#     where category='Front End'
# )as s
# on d.skill_code&s.code=s.code

# order by id

WITH TBL AS (
    SELECT SUM(CODE) AS SUM_CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT
    d.ID,
    d.EMAIL,
    d.FIRST_NAME,
    d.LAST_NAME
FROM
    DEVELOPERS d INNER JOIN TBL t
    ON d.SKILL_CODE & t.SUM_CODE > 0
ORDER BY
    d.ID ASC;