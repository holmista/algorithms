Create table Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
  declare @s int;
	--declare @N int = 88;
	with top5salaries as (
       select salary, dense_rank() over(order by salary desc) as number from Employee
	   )select @s =  salary FROM top5salaries WHERE number = @N
    RETURN (
	   isnull(@s,null)
    );
END