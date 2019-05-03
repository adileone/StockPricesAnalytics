DROP TABLE historical_stock_prices;
DROP TABLE first_query;


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

ADD FILE /media/alessandro/storage/big_data-primoProgetto/MapReduceScript/Job1/percentageChange_UDF.py;

CREATE TABLE first_query AS 

SELECT TRANSFORM (ticker,open,close ,adj_close,lowThe,highThe,volume,data)
            USING 'percentageChange_UDF.py'
            AS (ticker STRING,percentageIncrease DOUBLE,minimum_price DOUBLE,maximum_price DOUBLE,avgVolume DOUBLE)

FROM historical_stock_prices
WHERE data > "1998-01-01" AND data < "2018-01-01";

SELECT * 
FROM first_query
ORDER BY percentageIncrease DESC LIMIT 10;
