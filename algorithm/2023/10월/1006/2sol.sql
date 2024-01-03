-- solvesql 점검이 필요한 자전거

select
  bike_id
from
  rental_history
where
  date(rent_at) between '2021-01-01' and '2021-01-31'
group by bike_id
having
  sum(distance) >= 50000
