select distinct(id)
, email
, first_name
, last_name

from developers as d
join (
select * from skillcodes
    where category='Front End'
)as s
on d.skill_code & s.code = s.code

order by id