--https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial

-- 1
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950

--2
SELECT winner
  FROM nobel
 WHERE yr = 1962
   AND subject = 'literature'

--3
select yr, subject
from nobel
where winner = 'Albert Einstein'

--4
select winner
from nobel
where yr >= 2000 and subject = 'peace'

--5
select *
from nobel
where yr >= 1980 and yr <= 1989 and subject = 'Literature'

--6
SELECT *
FROM nobel
WHERE winner IN ('Theodore Roosevelt',
                  'Woodrow Wilson',
                  'Jimmy Carter',
                  'Barack Obama')

--7
select winner
from nobel
where winner like 'John%'

--8
select *
from nobel
where (subject = 'physics' and yr = 1980) or (subject = 'chemistry' and yr = 1984)

--9
select *
from nobel
where yr = 1980 and subject not in ('chemistry', 'medicine')

--10
select *
from nobel
where (subject = 'medicine' and yr < 1910) or (subject = 'Literature' and yr >= 2004)

--11
select *
from nobel
where winner = 'PETER GRÜNBERG'

--12
select *
from nobel
where winner like 'EUGENE O''NEILL'

--13
select winner, yr, subject
from nobel
where winner like 'Sir %' order by yr desc, winner

--14
SELECT winner, subject
FROM nobel
WHERE yr=1984
order by
    case
        when subject in ('Physics', 'Chemistry') then 1
        else 0
    end
    , subject
    , winner