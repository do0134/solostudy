-- 프로그래머스 헤비 유저가 소유한 장소

select
    *
from
    places p
where
    p.host_id in (select host_id from places a group by host_id having count(distinct id) >= 2)
order by
    id