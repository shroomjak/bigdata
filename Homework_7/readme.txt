1. Создал сборный tb файл пар xml+jpg из картинок и описаний к ним в папке при помощи gen_all_tb.py

2. Запустил обработку: hadoop-streaming-raw -input /BespyatyyIV/all.tb -output /BespyatyyIV/output_task_7 -mapper "/nn/bin/python ./mapper_raw.py"
Получил файл с парами true_label predicted_label

Результат:
guest@bigdata:~/BespyatyyIV/task_7$ hdfs dfs -cat /BespyatyyIV/output_task_7/part-00000
dog	dog
truck	ship
automobile	automobile
automobile	automobile
automobile	automobile
automobile	automobile
automobile	automobile
automobile	automobile
automobile	automobile
horse	horse
cat	airplane
deer	horse
truck	automobile
automobile	automobile
automobile	automobile
automobile	cat
automobile	truck
dog	horse
horse	horse
deer	automobile
deer	dog
deer	horse
deer	automobile
cat	cat
dog	automobile
truck	truck
dog	horse
automobile	horse
automobile	automobile
bird	horse
cat	dog
cat	ship
truck	automobile
automobile	dog
horse	truck
bird	airplane
automobile	automobile
deer	dog
airplane	automobile
bird	airplane
ship	ship
automobile	automobile
automobile	automobile
dog	dog
dog	dog
ship	truck
ship	truck
ship	truck
ship	airplane
ship	automobile
ship	airplane
ship	automobile
ship	truck
ship	truck
automobile	automobile
automobile	truck

3. Посчитал точность true/all: hadoop-streaming -input /BespyatyyIV/output_task_7 -output /BespyatyyIV/output_task_7_accuracy -mapper cat -reducer "/nn/bin/python /home/guest/BespyatyyIV/task_7/reducer_accuracy.py"

Результат:
guest@bigdata:~/BespyatyyIV/task_7$ hdfs dfs -cat /BespyatyyIV/output_task_7_accuracy/part-00000
accuracy	0.39	correct=22	total=56
