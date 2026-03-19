.mode csv
.separator ','
.import taxi.csv taxi -- добавил столбцы вручную
-- с учетом нулей
select avg(from1), avg(to1), avg(from2), avg(to2) from taxi;

-- без нулей
select avg(from1), avg(to1), avg(from2), avg(to2) from taxi where abs(from1) > 0
and abs(from2) > 0 and abs(to1) > 0 and abs(to2) > 0;