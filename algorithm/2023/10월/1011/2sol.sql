-- solvesql 레스토랑의 요일별 vip

select
  *
from
  tips a
where
  total_bill in (
    select
      total_bill
    from
      tips
    group by
      day
    having
      max(total_bill)
  )