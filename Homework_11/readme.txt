guest@bigdata:~/BespyatyyIV$ hadoop-streaming-tb --mapper "/nn/bin/python mapper.py" --reducer cat --input /datasets/toxic-comments-ru.seq --output /BespyatyyIV/task_10/

2026-05-22 16:14:23,166 INFO streaming.StreamJob: Output directory: /BespyatyyIV/task_10/
guest@bigdata:~/BespyatyyIV$ ls
class_tb	mapper.py  negative.csv		negpos_lstm.weights.h5	project		     task_3  task_5  task_7  trip_data_head.csv
keras_model.py	model.py   negpos_lstm.voc.npy	positive.csv		task_10_command.txt  task_4  task_6  task_9
guest@bigdata:~/BespyatyyIV$ ls task_9
cnn_dataset.tb	gen_tb.py  imdb_lstm.keras  imdb_lstm.voc.npy  imdb_lstm.weights.h5  mapper.py	view.py
guest@bigdata:~/BespyatyyIV$ cp ./task_9/view.py ./
guest@bigdata:~/BespyatyyIV$ ls
class_tb	mapper.py  negative.csv		negpos_lstm.weights.h5	project		     task_3  task_5  task_7  trip_data_head.csv
keras_model.py	model.py   negpos_lstm.voc.npy	positive.csv		task_10_command.txt  task_4  task_6  task_9  view.py
guest@bigdata:~/BespyatyyIV$ hadoop-streaming dumptb /BespyatyyIV/task_10/part-00000 | /nn/bin/python view.py
__label__NORMAL	потомучто,не было разносчиков заразы из-за границы. а у нас всё было под контролем и комары и клещи.	predict: 0.00
__label__INSULT	пиздаболы, сделали снимок, придумали историю и подали дурачкам через сми	predict: 1.00
__label__NORMAL	эти скаты ,на героев пионеров, анекдотов навыдумывали.	predict: 0.00
__label__NORMAL	да. я на нем за 21 день марафона скинула 5кг и обьемы ушли по 8см. а потом я чего то расслабилась в принципе как всегда и все. ((	predict: 0.00
__label__NORMAL	любовь....с первого взгляда..	predict: 0.00
__label__NORMAL	я сегодня проезжала по рабочей и между домами снитенко и гомолысовой магазином ( на пустыре) бежала кошка похожего окраса. может, я и ошиблась, но необычный окрас бросился в глаза.	predict: 0.00
__label__NORMAL	выглядеть аппетитно	predict: 0.00
__label__NORMAL	с праздником любимый город! процветания ! счастья всем жителям города! мирного неба над нашей страной!	predict: 1.00
__label__NORMAL	для вас ,я возьму на себя труд судить о вас ,по-моему большое открытие быть человеком￼ !!!!! если вы с такой беспардонности об этом говорить.	predict: 0.00
__label__NORMAL	грибок - что означает?	predict: 0.00
__label__INSULT,__label__OBSCENITY	хрен в жопу этому мудаку , а не респект	predict: 0.00
__label__INSULT,__label__OBSCENITY	вот рожа ее она еблась с узбеками и нарожала	predict: 0.00
__label__NORMAL	братка поздравляю тебя с днём рождения желаю всего и побольше а главное здоровья тебе и твоим близким	predict: 0.98
__label__NORMAL	и что на красной площади? раз в год 10 танков пройдут на резиновых траках? на автобанах только толщина подушки перед основным полотном больше метра, неважно где, германия, франция, чехия, венгрия и т.д.	predict: 0.00
__label__NORMAL	господи, как они надоели. всю ерунду выставляют. мы что рыбу не кушаем повашему? пусть себе кушает на здоровье раз купил. наверное разбогател чуть чуть.	predict: 0.00
__label__NORMAL	секс мосаж чтоли?	predict: 0.00
__label__NORMAL	пока хвалиться нечем , не очень хочется затевать ремонт в зале и в коридоре . сейчас много работы на огороде .	predict: 0.00
__label__INSULT	украина территория населенная ублюдками👎	predict: 0.00
__label__NORMAL	продали?,	predict: 0.00
__label__INSULT,__label__THREAT	заколоть этого плешивого урода что бы крякнул как селезень гандон штопанный всю вакцину ему в бошку что бы конкретно его завернуло	predict: 0.00
__label__NORMAL	это же надо так научить!!!👍👍😂😂	predict: 0.00
__label__NORMAL	как здорово! очень, очень рада за вас! 😊👍	predict: 0.93
__label__NORMAL	2 августа поздно вечером нашли вот такую потеряшку в районе высоток на победе. девочка явно домашняя, в новом ошейнике. обращаться +7 989 816-43-42	predict: 0.00
__label__NORMAL	какие жалкие	predict: 0.00
__label__NORMAL	с праздником дорогие, чистого неба над головой, мира на всей земле. спаси вас господь от шальных пуль.	predict: 0.00
__label__NORMAL	могу повторить. вы живёте в россии, не оставляйте российских детей без вашей заботы.	predict: 0.00
__label__NORMAL	кто заседать будет ..????	predict: 1.00
__label__NORMAL	еще как.каждый день свеженькую.	predict: 0.00
__label__INSULT	утырок,расскажи на какой параше тебя научили таким словам-люди стразу понимают,что ты конченая,безмозглая мразота,как епид говорит	predict: 0.07
__label__NORMAL	а что, карантин отменяется?	predict: 0.00
__label__NORMAL	вот это действительно красиво...	predict: 0.00
__label__NORMAL	ты минут пятнадцать назад смотрела сис приходил	predict: 0.00
__label__NORMAL	россия добрая - всё забудет, всё простит. он это понимает и по этому так себя ведёт.	predict: 0.00
__label__OBSCENITY	эти генеральши знают где соснуть и раздвинуть зад и передок ,позор страны	predict: 0.00
__label__NORMAL	ребята вы молодцы , так держать	predict: 1.00
__label__NORMAL	чё все так хватились за этого своего долбанного фургала, кто он такой - папа римский или губернатор чукотки? почему-то когда например сажают какую-нибудь девушку за превышение самообороны при защите от насильника, никто вот так не кукарекает.	predict: 0.00
__label__NORMAL	я тоже так считаю, что это большой грех. моя мама доживала со мной и когда заболела, я ухаживала за ней. а кто должен, как не дети?	predict: 0.00
__label__NORMAL	игорь ты с лазой не один	predict: 0.00
__label__NORMAL	чудо- художник!!! класс!!!	predict: 1.00
__label__NORMAL	детей бить - это преступление! очень жаль таких детишек,которые воспитываются с неадекватно- психическими отклонениями!	predict: 0.00
__label__NORMAL	ещё бы, ты на арбузах вырос	predict: 0.00
__label__INSULT	анна склярова (герасименкова) -- защитник я или не не тебе решать, а ты -- точно тупой вонючий тролль и старый пидорас пошёл нах !!!!!!!(tr)	predict: 0.00
__label__NORMAL	а мне зять подарил э/ простыню на дачу, теперь радуюсь каждую прохладную ночь, дивлюсь себе-зачем насморк заводила, когда есть такое чудо!	predict: 0.00
__label__NORMAL	красота..!! если есть, что показать??!! почему-нет!!???	predict: 0.98
__label__NORMAL	на 13 есть резины m+s	predict: 0.00
__label__NORMAL	с него первого и надо начинать! на пенсию его на минимальную	predict: 0.00
__label__NORMAL	ничего людей не учит*)	predict: 0.00
__label__INSULT	нахуй тут нужен этот заслуженный оленевод володи	predict: 0.00
__label__NORMAL	классный сериал клон 👍👍👍👍⭐⭐⭐⭐⭐	predict: 0.00
__label__NORMAL	ретро дежавю ... сложно понять чужое сердце , лиш ощутить музыкой видимо	predict: 0.00
