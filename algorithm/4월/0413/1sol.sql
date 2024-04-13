-- HackerRank Contest Leaderboard

select s.hacker_id,h.name, sum(s.max_score) as total_score
from (select hacker_id, max(score) as max_score from submissions group by challenge_id, hacker_id) as s
join hackers h on s.hacker_id = h.hacker_id
group by s.hacker_id, h.name
having sum(s.max_score) > 0
order by total_score desc, s.hacker_id