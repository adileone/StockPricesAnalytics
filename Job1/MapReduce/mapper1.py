import sys
from datetime import datetime as dt


check = {}
checkVolume={}

infile = sys.stdin

#skip first line of input file
next(infile)

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker,open_pr,close ,adj_close,lowThe,highThe,volume,data = line.split(',')

    date = dt.strptime(data, "%Y-%m-%d")
    start = dt.strptime("1998-01-01", "%Y-%m-%d")
    end = dt.strptime("2018-01-01", "%Y-%m-%d")

    if ((date > start) and (date < end)):

        if ticker not in check.keys():
            check[ticker]=[]
    
        check[ticker].append(float(close))

        if ticker not in checkVolume.keys():
            checkVolume[ticker]=[]
    
        checkVolume[ticker].append(float(volume))
        
for key in check.keys():
    print "{} {} {} {} {} {}".format(key, check[key][0], check[key][-1], min(check[key]), max(check[key]), sum(checkVolume[key]) / len(checkVolume[key]) )
