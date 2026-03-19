обновления:
поменял структуру папок в ~/BespyatyyIV, теперь там task_3 и task_4

загрузка через scp на локальной машине
scp reducer.c guest@37.204.230.20:/home/guest/BespyatyyIV/task_4/
scp mapper.py guest@37.204.230.20:/home/guest/BespyatyyIV/task_4/

компиляция кода на c:

guest@bigdata:~/BespyatyyIV/task_4$ gcc -o reducer reducer.c

запуск:

guest@bigdata:~$ hadoop-streaming  -input /datasets/twitter/positive-ru.csv -mapper "python3 /home/guest/BespyatyyIV/task_4/mapper.py" -reducer "/home/guest/BespyatyyIV/task_4/reducer" -output /BespyatyyIV/result_task4/

результаты:

guest@bigdata:~$ hdfs dfs -cat /BespyatyyIV/result_task4/part-00000
posts	114911
total_words	1440694
avg_words	12.5

код писал при помощи чатика, но зато разобрался как работает map reduce и в чем особенность считывания при помощи sys.stdin. запросов было несколько, прикреплять все не буду, слишком много текста

map - мапперы работают независимо, на блоках, на которые разделяет файлы файловая система hadoop, выдают пары ключ - значение (что и есть map)

затем происходит сортировка выходов из мапперов по ключам, и выходы с одинаковыми ключами идут в один и тот же reducer

поэтому на выходе моего маппера записи вида all num1 num2, где all -- ключ, num1 -- число слов в считанных постах, num2 -- число постов. в данном случае число постов num2 всегда равно одному, так как считываем мы построчно, а одна строка = один пост в csv файле

