select h.flavor
from (select flavor, sum(TOTAL_ORDER) as total
    from FIRST_HALF
    group by flavor
) as h
join
(select flavor, sum(TOTAL_ORDER) as total
    from july
    group by flavor
) as j
on h.flavor=j.flavor
group by flavor 

order by (h.total + j.total)desc

limit 3


# strawberry, chocolate, white_chocolate