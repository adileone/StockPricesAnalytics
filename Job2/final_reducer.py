#!/usr/bin/env python2
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
    
    sector=words[0]
    year=int(words[1])
    close=float(words[2])
    volume=float(words[3])

    if (year,sector) not in checkClose.keys():
        checkClose[(year,sector)]=[]
        checkClose[(year,sector)].append(close)
        checkClose[(year,sector)].append(1)

    else :
        checkClose[(year,sector)][0]+=close
        checkClose[(year,sector)][1]+=1

    if (year,sector) not in checkVolume.keys():
        checkVolume[(year,sector)]=0
    
    checkVolume[(year,sector)]+=volume

for key in checkClose.keys():

    if key not in myDict.keys():
        myDict[key]=[]
    
    myDict[key].append(checkVolume[key])
    myDict[key].append(checkClose[key][0])
    avgDailyQuote=checkClose[key][0]/checkClose[key][1]
    myDict[key].append(avgDailyQuote)

for (year,sector) in myDict.keys():

    try:
        a=float(myDict[(year-1,sector)][1])
        b=float(myDict[(year,sector)][1])
        
        myDict[(year,sector)].append(round(100*(b-a)/a, 2))
        
    except:
        myDict[(year,sector)].append(0)
        continue

sorted_by_value = sorted(myDict, key = lambda k: (k[1], k[0]), reverse=True)

for el in sorted_by_value:    
    print "{}\t{}\t{}\t{}%\t{}".format(el[0],el[1] ,myDict[el][0], myDict[el][3], myDict[el][2])
