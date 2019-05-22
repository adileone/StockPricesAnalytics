import sys

infile = sys.stdin

checkClose={}
checkVolume={}
myDict={}

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split('|')
    
    ticker=words[0]
    close=float(words[1])
    year=int(words[2])
    sector=words[3]
    
    if (ticker,year,sector) not in checkClose.keys():
        checkClose[(ticker,year,sector)]=[]
        checkClose[(ticker,year,sector)].append(close)
        checkClose[(ticker,year,sector)].append(0)
               
    else :
        checkClose[(ticker,year,sector)][0]+=close

for (ticker,year,sector) in checkClose.keys():

    try:
        a=float(checkClose[(ticker,year-1,sector)][0])
        b=float(checkClose[(ticker,year,sector)][0])
        
        checkClose[(ticker,year,sector)][1]+=(round(100*(b-a)/a))
        
    except:
        checkClose[(ticker,year,sector)][1]+=0
        continue

sorted_by_value = sorted(checkClose, key = lambda k: (k[0], k[1]), reverse=True)

for el in sorted_by_value:    
    print "{}|{}|{}|{}".format(el[0],el[1],el[2],checkClose[el][1])
