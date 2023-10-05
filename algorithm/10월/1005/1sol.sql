-- 레스토랑 웨이터 팁

select
  day,
  time,
  round(avg(tip), 2) as avg_tip,
  round(avg(size), 2) as avg_size
from
  tips
group by
  day,
  time