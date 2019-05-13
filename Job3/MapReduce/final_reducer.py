#!/usr/bin/env python2
import sys

check={}

infile = sys.stdin

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker,data,percentage,sector = line.split('|')

    if ticker not in check.keys():
        check[ticker] = {}
        check[ticker]['sector'] = sector
        check[ticker][data] = percentage 
    else :
        check[ticker][data] = percentage 

for key in check.keys():
    if '2016'  not in check[key].keys():
        del check[key]
        continue
    if '2017'  not in check[key].keys():
        del check[key]
        continue
    if '2018'  not in check[key].keys():
        del check[key]

myDict={}
for key in check.keys():
    myDict[key]=[check[key]['sector'],check[key]['2016'],check[key]['2017'],check[key]['2018']]

checkList = []        

for key in myDict.keys():
    for key1 in myDict.keys():
        if (key != key1) and (check[key]['sector']!=check[key1]['sector']) \
                        and (check[key]['2016']==check[key1]['2016']) \
                        and (check[key]['2017']==check[key1]['2017']) \
                        and (check[key]['2018']==check[key1]['2018']) :
            
            if (key,key1) not in checkList:
                checkList.append((key,key1))
                checkList.append((key1,key))
                print "{},{},2016:{}%, 2017:{}%, 2018:{}%".format(key,key1,check[key]['2016'],check[key]['2017'],check[key]['2018'])    