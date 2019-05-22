#!/usr/bin/python3

from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import year
from pyspark.sql import functions as F
from pyspark.sql.window import Window

startTime = datetime.now()

spark = SparkSession.builder.appName('abc').getOrCreate()

stock_prices = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED').load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/X1_historical_stock_prices.csv")

stocks = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED').load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/X1_historical_stocks.csv")

stock_prices=stock_prices.select('ticker','close','volume',year("date").alias('year'))

stocks=stocks.select('ticker','sector')

joined = stock_prices.join(stocks, on='ticker')

filtered = joined.filter((joined.year <= '2018') & (joined.year >= '2004') & (joined.sector != 'N/A'))

intermediate1 = filtered.groupBy('sector','year').agg(F.sum(filtered.volume).alias('volCompl'),F.mean(filtered.close).alias('avg_volume'))

intermediate1 = intermediate1.sort(F.desc('sector'),F.desc('year'))

intermediate2 = filtered.groupBy('sector','year').agg(F.sum(filtered.close).alias('actualQuote'))

intermediate2 = intermediate2.sort(F.desc('sector'),F.desc('year'))

intermediate3 = intermediate2.withColumn('previousQuote',F.lead('actualQuote').over(Window.partitionBy('sector').orderBy(F.desc('sector'),F.desc('year'))))

intermediate3 = intermediate3.sort(F.desc('sector'),F.desc('year'))

result = intermediate3.withColumn('percentage',(100*(intermediate3['actualQuote'] - intermediate3['previousQuote']) / intermediate3['previousQuote']) )

result = result.join(intermediate1, on=['sector','year'])

result = result.select('sector','year','volCompl','percentage','avg_volume')

result = result.sort(F.desc('sector'),F.desc('year'))

result.show(15,truncate= True)

print('Exec Time: ', datetime.now() - startTime)

