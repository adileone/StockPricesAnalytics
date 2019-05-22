#!/usr/bin/python3

from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

startTime = datetime.now()

spark = SparkSession.builder.appName('abc').getOrCreate()

dataFrame = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED').load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stock_prices.csv")

df = dataFrame.filter((dataFrame.date < '2018-01-01') & (dataFrame.date > '1998-01-01'))

df = df.select('ticker','close', 'volume', 'date')

df1 = df.groupBy('ticker').agg((100*(F.last(df.close)-F.first(df.close))/F.first(df.close)).alias('percentageIncrease'),
                               F.min(df.close).alias('min_close'), 
                               F.max(df.close).alias('max_close'),
                               F.mean(df.volume).alias('avg_volume'))

final = df1.orderBy(df1['percentageIncrease'].desc())

final.show(10)

print('Exec Time: ', datetime.now() - startTime)
