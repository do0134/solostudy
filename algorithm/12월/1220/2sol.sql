-- leetcode 184. Department Highest Salary
select de.name as Department, e1.name as Employee, e1.salary as Salary 
from Employee e1, Department de
where de.id = e1.departmentId and e1.salary = (select max(salary) from Employee where departmentId = de.id)