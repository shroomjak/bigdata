1. Создал tb файл из csv при помощи скрипта gen_tb.py:

hdfs dfs -cat /datasets/cnn_dataset.csv | /nn/bin/python gen_tb.py | hdfs dfs -put - /BespyatyyIV/task_9/cnn_dataset.tb

2. Запустил обработку:

hadoop-streaming-raw -input /BespyatyyIV/task_9/cnn_dataset.tb -output /BespyatyyIV/task_9_output/ -mapper "/nn/bin/python ./mapper.py"
