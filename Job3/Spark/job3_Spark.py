#!/usr/bin/python3

from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import year
from pyspark.sql import functions as F
from pyspark.sql.window import Window

startTime = datetime.now()

spark = SparkSession.builder.appName('abc').getOrCreate()

stock_prices = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED')\
.load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stock_prices.csv")

stocks = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED')\
.load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stocks.csv")

stock_prices=stock_prices.select('ticker','close',year("date").alias('year'))

stocks=stocks.select('ticker','sector')

joined = stock_prices.join(stocks, on='ticker')

filtered = joined.filter((joined.year <= '2018') & (joined.year >= '2015') & (joined.sector != 'N/A'))

intermediate1 = filtered.groupBy('ticker','year','sector').agg(F.sum(filtered.close).alias('actualQuote'))

intermediate1 = intermediate1.sort(F.desc('ticker'),F.desc('year'))

intermediate2 = intermediate1.withColumn('previousQuote',F.lead('actualQuote').over(Window.partitionBy('ticker').orderBy(F.desc('ticker'),F.desc('year'))))

intermediate2 = intermediate2.sort(F.desc('ticker'),F.desc('year'))

intermediate3 = intermediate2.withColumn('percentage',F.round(100*(intermediate2['actualQuote'] - intermediate2['previousQuote']) / intermediate2['previousQuote']))

intermediate3 = intermediate3.select('ticker','year','sector','percentage')

intermediate3 = intermediate3.sort(F.desc('ticker'),F.desc('year'))

intermediate3 = intermediate3.filter((intermediate3.year != '2015'))

intermediate4 = intermediate3.groupBy('ticker','sector').agg(F.collect_list(intermediate3.percentage).alias('trend'))

intermediate4 = intermediate4.filter(F.size(intermediate4.trend) == 3)

result = intermediate4.alias('l').join(intermediate4.alias('r'), on='trend')\
    .where('r.sector != l.sector')\
    .select(F.col('l.ticker').alias('ticker1'), F.col('r.ticker').alias('ticker2'), 'l.trend')

result = result.sort('ticker1','ticker2') 

result.show(26)

print('Exec Time: ', datetime.now() - startTime)
