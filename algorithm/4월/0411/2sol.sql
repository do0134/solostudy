-- HackerRank Weather Observation Station 8

select distinct
    city
from station
where
    city regexp '^(a|e|o|u|i)'
and
    city regexp '(a|e|o|u|i)$'