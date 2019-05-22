DROP TABLE historical_stock_prices;

CREATE TABLE  historical_stock_prices (ticker STRING, 
                                                    open DOUBLE, 
                                                    close DOUBLE, 
                                                    adj_close DOUBLE, 
                                                    lowThe DOUBLE, 
                                                    highThe DOUBLE, 
                                                    volume DOUBLE, 
                                                    data DATE)

ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';                                                    

LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/historical_stock_prices.csv' OVERWRITE INTO TABLE historical_stock_prices; 

ADD JAR /media/alessandro/storage/big_data-primoProgetto/MapReduceScript/Job1/myUDAF.jar; 

CREATE TEMPORARY FUNCTION compIncrease AS 'compute_increaseUDAF.Compute';


SELECT ticker, compIncrease(data, close) as percentageIncrease, MIN(close) as minimum, MAX(close) as maximum, AVG(volume) as avg_volume
FROM historical_stock_prices
WHERE data > "1998-01-01" AND data < "2018-01-01"
GROUP BY ticker
ORDER BY percentageIncrease DESC LIMIT 10; 

