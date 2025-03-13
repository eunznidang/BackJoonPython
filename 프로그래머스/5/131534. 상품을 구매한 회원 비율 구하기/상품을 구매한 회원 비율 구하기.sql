select year(o.sales_date), month(o.sales_date), count(distinct(o.user_id))
, round((count(distinct(o.user_id))/s.cnt),1 )
from online_sale as o
join (select
     count(*) cnt
      from user_info
      where year(joined)=2021)as s
     
where user_id in(
select user_id from user_info 
where year(joined)=2021)

group by  year(sales_date), month(sales_date)

order by year(sales_date), month(sales_date)