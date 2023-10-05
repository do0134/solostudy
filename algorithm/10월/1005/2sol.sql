-- solvesql 레스토랑의 일일매출

select
  day,
  sum(total_bill) as revenue_daily
from
  tips
group by
  day
having
  revenue_daily >= 1000
order by
  revenue_daily desc