1. Создал файл в своей рабочей папке keras_model.py
2. Проверил работу на одном примере из папки ~/test2026:

guest@bigdata:~$ /nn/bin/python ./BespyatyyIV/keras_model.py < ./test2026/00001.jpg 
2026-04-03 21:44:26.695298: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1775241866.716352   99353 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1775241866.722874   99353 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2026-04-03 21:44:26.743685: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2026-04-03 21:44:28.996560: E external/local_xla/xla/stream_executor/cuda/cuda_driver.cc:152] failed call to cuInit: INTERNAL: CUDA error: Failed call to cuInit: UNKNOWN ERROR (303)
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 120ms/step
5

3. Запустил hadoop-streaming-raw

guest@bigdata:~$ hadoop-streaming-raw -mapper '/nn/bin/python ~/BespyatyyIV/keras_model.py' -input /sample/ -output /BespyatyyIV/cifar10_test.txt

Результат в папке /BespyatyyIV/cifar10_test.txt/ (плохое название, не понял как переименовать)

guest@bigdata:~$ hadoop fs -cat /BespyatyyIV/cifar10_test.txt/part-00000
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 119ms/step
9


