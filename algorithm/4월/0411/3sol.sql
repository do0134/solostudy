-- HackerRank Higher Than 75 Marks

select name
from students
where
    marks > 75
order by
    substring(name, -3), id