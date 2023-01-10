-- leetcode 595. Big Countries
select w.name, w.population, w.area from World w where (w.area >= 3000000) or (w.population >= 25000000) 