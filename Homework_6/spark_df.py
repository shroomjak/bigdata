from pyspark.sql import SparkSession
from pyspark.sql.functions import mean


filename = 'task1data.csv'

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read
    .option('header', True)
    .option('sep', ',')
    .option('inferSchema', True)
    .csv(filename)
)

result = df.agg(
    mean('temp1').alias('avg_temp'),
    mean('frequency0').alias('avg_freq')
)

result.show()
spark.stop()