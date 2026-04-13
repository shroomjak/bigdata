from pyspark.sql import SparkSession


filename = 'task1data.csv'

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read
    .option('header', True)
    .option('sep', ',')
    .option('inferSchema', True)
    .csv(filename)
)

df.createOrReplaceTempView('data')

result = spark.sql(
    """
    SELECT
        AVG(temp1) AS avg_temp,
        AVG(frequency0) AS avg_freq
    FROM data
    """
)

result.show()
spark.stop()