Create table Stadium (id int, visit_date DATE NULL, people int)
Truncate table Stadium
insert into Stadium (id, visit_date, people) values ('1', '2017-01-01', '10')
insert into Stadium (id, visit_date, people) values ('2', '2017-01-02', '109')
insert into Stadium (id, visit_date, people) values ('3', '2017-01-03', '150')
insert into Stadium (id, visit_date, people) values ('4', '2017-01-04', '99')
insert into Stadium (id, visit_date, people) values ('5', '2017-01-05', '145')
insert into Stadium (id, visit_date, people) values ('6', '2017-01-06', '1455')
insert into Stadium (id, visit_date, people) values ('7', '2017-01-07', '199')
insert into Stadium (id, visit_date, people) values ('8', '2017-01-09', '188')

with cte1 as(
select s.id,s.visit_date,s.people,
ROW_NUMBER() over(order by s.id) as num
from Stadium s
where s.people>=100
),cte2 as( select *,id-num as diff from cte1)
,cte3 as (select *,count(diff) over(partition by diff) as repeats from cte2)
select id,visit_date,people from cte3 where repeats>=3