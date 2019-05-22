import sys

infile = sys.stdin

#skip first line of input file
next(infile)

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split(',')

    # Only can we recognize relations by the number of their columns
    if (len(words) == 8):
        # this is a row in file historical_stock_prices.csv
        ticker,open_pr,close ,adj_close,lowThe,highThe,volume,data = words

        print "{}|{}|{}|{}|-".format(ticker,close,volume,data)
    else:
        # This must be a row in file historical_stocks.csv
        if (len(words)==6):
            ticker,exchange,name,void,sector,industry = words
        if (len(words)==5):
            ticker,exchange,name,sector,industry = words

        print "{}|-|-|-|{}".format(ticker,sector)
