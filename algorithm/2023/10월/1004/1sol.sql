-- solvesql 복수 국적 메달 수상한 선수찾기

select a.name from records r
join athletes a
on a.id = r.athlete_id
join games g
on r.game_id = g.id and g.year >= 2000
where medal is not null
group by a.id
having count(distinct r.team_id) > 1
order by name