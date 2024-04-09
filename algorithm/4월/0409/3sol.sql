-- HackerRank SoftwareEnginner test1

select
    id, first_name, last_name
from
    customer
where
    length(first_name)+length(last_name) < 12
order by
    length(first_name)+length(last_name), concat(first_name,last_name), id
