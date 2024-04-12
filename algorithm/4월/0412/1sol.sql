-- HackerRank Population Census

select
    sum(c.population)
from
    city c
left join
    country ctry
on
    c.countrycode = ctry.code
where
    ctry.continent = "Asia"