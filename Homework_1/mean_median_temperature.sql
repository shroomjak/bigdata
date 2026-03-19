.mode csv
.separator ';'
.import log.csv log

pragma table_info(log); -- Узнаем названия столбцов

select avg(temp1) from log; -- среднее
-- 44.8202092511013

select avg(val)
from(
	select temp1 as val
	from log
	order by temp1
	limit 2 - (select count(*) from log) % 2 -- 2 если четное, 1 если нечетное
	offset (select (count(*) - 1) / 2 from log)
);