-- solvesql 일별 블로그 방문자수 집계

select strftime('%Y-%m-%d', event_date_kst) as dt, count(distinct user_pseudo_id) as users
from ga
where dt >= '2021-08-02' and dt <= '2021-08-09'
group by dt
order by dt asc