-- HackerRank Weather Observation Station 4

select
count(city) - count(distinct city)
from
station