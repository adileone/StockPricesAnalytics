DROP TABLE historical_stock_prices;
DROP TABLE historical_stocks;
DROP TABLE joined;
DROP TABLE semifinal;
DROP TABLE t1;
DROP TABLE t2;

CREATE TEMPORARY TABLE historical_stock_prices (ticker STRING, 
                                                    open DOUBLE, 
                                                    close DOUBLE, 
                                                    adj_close DOUBLE, 
                                                    lowThe DOUBLE, 
                                                    highThe DOUBLE, 
                                                    volume DOUBLE, 
                                                    data STRING)


ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';                                                    
LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stock_prices.csv' OVERWRITE INTO TABLE historical_stock_prices; 

CREATE TEMPORARY TABLE historical_stocks (ticker STRING,market STRING,name STRING,sector STRING,industry STRING)

ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\"");                                                 
LOAD DATA LOCAL INPATH '/media/alessandro/storage/big_data-primoProgetto/dataset/X3_historical_stocks.csv' OVERWRITE INTO TABLE historical_stocks;

CREATE TEMPORARY TABLE joined AS 
SELECT f.ticker as ticker, f.close as close, f.volume as volume, YEAR(f.data) as data, l.sector as sector
FROM
    historical_stock_prices as f JOIN historical_stocks as l ON f.ticker=l.ticker
WHERE l.sector != 'N/A' AND data > '2004-01-01' AND data < '2018-12-31'; 

CREATE TEMPORARY TABLE semifinal AS
SELECT sector, data, sum(volume) as volCompl, avg(close) as meanClose
FROM joined
GROUP BY sector, data
ORDER BY sector, data DESC;  

CREATE TEMPORARY TABLE t1 AS
SELECT sector, data, sum(close) as sumClose
from joined
GROUP BY sector, data
ORDER BY sector DESC, data DESC;

CREATE TEMPORARY TABLE t2  AS
    SELECT 
        j.sector, 
        j.data, 
        t.sumClose as attuale, 
        lead(t.sumClose, 1) over (partition by j.sector order by j.sector, j.data DESC) as precedente
    FROM 
        semifinal as j JOIN t1 as t on j.sector=t.sector and j.data=t.data

    GROUP BY j.sector, j.data, t.sumClose
    ORDER BY j.sector DESC, j.data DESC;  


SELECT s.sector, s.data, (100*(t2.attuale-t2.precedente)/t2.precedente) as percentage, s.volCompl, s.meanClose 
FROM semifinal as s join t2 on s.sector = t2.sector and s.data=t2.data
LIMIT 15;
