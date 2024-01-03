-- solvesql 두테이블 결합하기

select distinct r.athlete_id
from records r
join events e
on (r.event_id = e.id and e.sport = "Golf")