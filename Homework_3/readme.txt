scp mapper.py guest@37.204.230.20:/home/guest/BespyatyyIV/
ввел пароль

scp reducer.py guest@37.204.230.20:/home/guest/BespyatyyIV/
ввел пароль

ssh guest@37.204.230.20
ввел пароль
зашел как guest

проверил данные:
hdfs dfs -cat /datasets/nyc-taxi-latlon/trip_data_head.csv | head -10 | python3 ~/BespyatyyIV/mapper.py

поменял индексы в коде с 6:8 на 10:12, но лучше не хардкодить а искать через index, но уже ладно
загрузил еще раз mapper.py через scp как выше из другого терминала

запустил
hadoop-streaming  -input /datasets/nyc-taxi-latlon/trip_data_head.csv -mapper "python3 /home/guest/BespyatyyIV/mapper.py" -reducer "python3 /home/guest/BespyatyyIV/reducer.py" -output /BespyatyyIV/result_task3

hdfs dfs -cat /BespyatyyIV/result_task3/part-00000
Total lines: 9	
Mean pickup_longitude: -73.985885	
Mean pickup_latitude:  40.749349	

