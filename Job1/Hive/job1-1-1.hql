DROP TABLE historical_stock_prices;
DROP TABLE filtered;
DROP TABLE firstClose;
DROP TABLE lastClose;
DROP TABLE agggregated;
DROP TABLE toJoin;


CREATE TABLE  historical_stock_prices (ticker STRING, 
                                                    open DOUBLE, 
                                                    close DOUBLE, 
                                                    adj_close DOUBLE, 
                                                    lowThe DOUBLE, 
                                                    highThe DOUBLE, 
                                                    volume DOUBLE, 
                                                    data STRING)

ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';                                                    

LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stock_prices.csv' OVERWRITE INTO TABLE historical_stock_prices; 

CREATE TABLE filtered AS 
SELECT  ticker,close,volume,data
FROM    historical_stock_prices
WHERE   data > '1998-01-010' AND data < '2018-01-01';

CREATE TABLE firstClose AS
select * from (
select ticker,close,volume,data,
rank() over ( partition by ticker order by data asc) as rank
FROM filtered ) t 
WHERE rank = 1;

CREATE TABLE lastClose AS
select * from (
select ticker,close,volume,data,
rank() over ( partition by ticker order by data desc) as rank
FROM filtered ) t 
WHERE rank = 1;

CREATE TABLE agggregated AS 
SELECT DISTINCT
    f.ticker, (100*(l.close-f.close)/f.close) as percentageIncrease
FROM
    firstClose as f JOIN lastClose as l ON f.ticker=l.ticker
ORDER BY percentageIncrease desc; 

CREATE TABLE toJoin AS 
SELECT 
    ticker, MIN(close) as minimum, MAX(close) as maximum, AVG(volume) as avg_volume
FROM 
    filtered
GROUP BY ticker;

SELECT 
    a.ticker, a.percentageIncrease, j.minimum , j.maximum, j.avg_volume
FROM 
    agggregated as a JOIN toJoin as j ON a.ticker=j.ticker
ORDER BY 
    percentageIncrease DESC LIMIT 10;
