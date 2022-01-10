Create table Employee (id int, name varchar(255), salary int, departmentId int)
Create table Department (id int, name varchar(255))
Truncate table Employee
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1')
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1')
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2')
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2')
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1')
Truncate table Department
insert into Department (id, name) values ('1', 'IT')
insert into Department (id, name) values ('2', 'Sales')

with maxSalaries as (
select d.id, max(salary) maxSalary
from Employee e
join Department d on e.departmentId=d.id
group by d.id
)
select d.name Department,e.name Employee,Salary from maxSalaries m join
Employee e on e.departmentId=m.id join Department d
on e.departmentId=d.id where e.salary=m.maxSalary