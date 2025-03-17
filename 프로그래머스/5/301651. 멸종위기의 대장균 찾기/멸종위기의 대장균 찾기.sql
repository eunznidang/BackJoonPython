with recursive 세대 as(
select id, parent_id, 1 as depth
    from ecoli_data
    where parent_id is null
    
    union all
    
    select c.id, c.parent_id, p.depth+1
    from ecoli_data c
    join 세대 p on c.parent_id=p.id
)

select count(*) count
,depth generation from 세대
where id not in (select distinct parent_id
                from 세대
                ecoli_data
                where parent_id is not null)
group by depth