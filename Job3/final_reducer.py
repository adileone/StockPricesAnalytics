#!/usr/bin/env python2
import sys

check={}

infile = sys.stdin

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker,percentage,sector = line.split('|')

    if ticker not in check.keys():
        check[ticker] = []
        check[ticker].append(sector)
        check[ticker].append(percentage)
    else :
        check[ticker].append(percentage)

for key in check.keys():
    if (len(check[key])!=4):
        del check[key]

checkList = []        

for key in check.keys():
    for key1 in check.keys():
        if (key != key1) and (check[key][0]!=check[key1][0]) \
                        and (check[key][1]==check[key1][1]) \
                        and (check[key][2]==check[key1][2]) \
                        and (check[key][3]==check[key1][3]) :
            
            if (key,key1) not in checkList:
                checkList.append((key,key1))
                checkList.append((key1,key))
                print "{},{},2016:{}%, 2017:{}%, 2018:{}%".format(key,key1,check[key][1],check[key][2],check[key][3])
    