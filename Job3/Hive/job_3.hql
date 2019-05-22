DROP TABLE historical_stock_prices;
DROP TABLE historical_stocks;
DROP TABLE joined;
DROP TABLE projection;
DROP TABLE percentage;
DROP TABLE trends;

CREATE TABLE IF NOT EXISTS historical_stock_prices (ticker STRING, 
                                                    open DOUBLE, 
                                                    close DOUBLE, 
                                                    adj_close DOUBLE, 
                                                    lowThe DOUBLE, 
                                                    highThe DOUBLE, 
                                                    volume DOUBLE, 
                                                    data STRING)


ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';                                                    
LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stock_prices.csv' OVERWRITE INTO TABLE historical_stock_prices; 

CREATE TABLE IF NOT EXISTS historical_stocks (ticker STRING,market STRING,name STRING,sector STRING,industry STRING)

ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\"");                                                 
LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stocks.csv' OVERWRITE INTO TABLE historical_stocks;

CREATE TABLE IF NOT EXISTS joined AS 
SELECT f.ticker as ticker, l.sector as sector, f.close as close, YEAR(f.data) as data
FROM
    historical_stock_prices as f JOIN historical_stocks as l ON f.ticker=l.ticker
WHERE l.sector != 'N/A' AND data >= '2015-01-01' AND data <= '2018-12-31';

CREATE TABLE IF NOT EXISTS projection  AS
    SELECT 
        ticker, 
        data,
        sector, 
        sum(close) as actual, 
        lead(sum(close), 1) over (partition by ticker order by ticker, data DESC) as previous
    FROM 
        joined

    GROUP BY ticker, data, sector
    ORDER BY ticker DESC, data DESC;

CREATE TABLE IF NOT EXISTS percentage  AS
    SELECT 
        ticker, data, sector, cast(round(100*(actual-previous)/previous) as STRING) as percentage               
    FROM 
        projection
    ORDER BY ticker DESC, data DESC;  

CREATE TABLE IF NOT EXISTS trends  AS
SELECT ticker, sector, collect_list(percentage) as trend
FROM percentage
WHERE data != "2015"
GROUP BY ticker,sector;

SELECT t1.ticker,t2.ticker,concat_ws(',',t1.trend) as commonTrend 
FROM trends t1 JOIN trends t2 on t1.trend = t2.trend
WHERE size(t1.trend) = 3 and t1.sector!=t2.sector
GROUP BY t1.ticker,t2.ticker,t1.trend
ORDER BY t1.ticker,t2.ticker;
