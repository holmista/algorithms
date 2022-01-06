Create table Employee (id int, salary int)
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

declare @highest int
declare @secondHighest int
select @highest = max(salary) from Employee
select @secondHighest =  max(salary) from Employee where salary !=@highest
select @secondHighest as SecondHighestSalary