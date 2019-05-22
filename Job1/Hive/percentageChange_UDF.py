#!/usr/bin/env python2
import sys

## we are receiving each record passed in from Hive via standard input 
## By default, columns will be transformed to STRING and delimited by TAB 
## Also, by default, NULL values will be converted to literal string \N to differentiate from empty strings

check = {}
volumes = dict()

#.readlines()
for line in sys.stdin:
    
    line = line.strip("\n ")
    
    ticker,open_pr,close ,adj_close,lowThe,highThe,volume,data = line.split("\t")
    
    if ticker not in check.keys():
        check[ticker]=[]
    
    check[ticker].append(float(close))

    if ticker not in volumes.keys():
        volumes[ticker]=[]
    
    volumes[ticker].append(float(volume))

for key in check.keys():

    a=check[key][0]
    b=check[key][-1]

    percentage = round(100*(b-a)/a, 2)
    minimum_price = min(check[key])
    maximum_price = max(check[key])
    avg = sum(volumes[key]) / len(volumes[key]) 

    print "{}\t{}\t{}\t{}\t{}".format(key,percentage,round(minimum_price,4),round(maximum_price,3),round(avg,2))
     