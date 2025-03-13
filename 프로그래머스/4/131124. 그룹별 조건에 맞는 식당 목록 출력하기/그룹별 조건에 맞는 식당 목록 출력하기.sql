# -- 코드를 입력하세요
SELECT p.MEMBER_NAME
, r.REVIEW_TEXT
, date_format(r.REVIEW_DATE,'%Y-%m-%d') as review_date

from rest_review r
join member_profile p
on r.member_id=p.member_id

where r.member_id in(
select member_id
from (
    SELECT member_id, 
       RANK() OVER (ORDER BY COUNT(review_id) DESC) AS ranking
FROM rest_review
GROUP BY member_id
) as t

where t.ranking=1
)

order by r.REVIEW_DATE, r.REVIEW_TEXT

