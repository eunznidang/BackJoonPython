SELECT DISTINCT(D.ID)
, D.EMAIL
, D.FIRST_NAME
, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN SKILLCODES AS S
ON D.SKILL_CODE & S.CODE
WHERE S.NAME='C#'
OR S.NAME='Python'
ORDER BY ID