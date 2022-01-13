Create table Seat (id int, student varchar(255))
Truncate table Seat
insert into Seat (id, student) values ('1', 'Abbot')
insert into Seat (id, student) values ('2', 'Doris')
insert into Seat (id, student) values ('3', 'Emerson')
insert into Seat (id, student) values ('4', 'Green')
insert into Seat (id, student) values ('5', 'Jeames')

with cte1 as(
select case when id%2=1 then id+1 else id-1 end as id,student from Seat
),cte2 as( select *,isnull(lag(id) over(order by id),0) prev from cte1)
select case when id-prev>1 then id-1 else id end as id,student  from cte2