#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:32:15 2018

@author: mingchien
"""

from kafka import KafkaConsumer
import sqlite3
import json

def toint(value):
  try:
    intType=int(value)
    return intType
  except:
    return value

def insertDictSQL(row):   
    if row['cost'] is None:
        insertSQLtoSQLite = '''
            insert into CROWDINSIGHT_AIRLINE_INFO(
            "ID",
        	"AVIATION",
        	"FLIGHT",
        	"ROUTE",
        	"DEPARTURE",
        	"ARRIVAL",
        	"DEPARTURE_TIME",
        	"ARRIVAL_TIME",
        	"MODEL",
        	"TICKET",
        	"COST",
        	"FLIGHT_DATE",
        	"CRAWL_DATE")
            VALUES(
            "%s","%s","%s","%s","%s","%s",
            "%s","%s","%s","%s","%d","%s","%s");
            '''%(row['id'],row['aviation'],row['flight'],row['route'],row['departure'],row['arrival'],row['departure_time'],row['arrival_time'],row['model'],row['ticket'],0,row['flight_date'],row['crawl_date'])
        SQLite_cursor.execute(insertSQLtoSQLite)
        
        return SQLite_cursor 
    else:
        insertSQLtoSQLite = '''
            insert into CROWDINSIGHT_AIRLINE_INFO(
            "ID",
        	"AVIATION",
        	"FLIGHT",
        	"ROUTE",
        	"DEPARTURE",
        	"ARRIVAL",
        	"DEPARTURE_TIME",
        	"ARRIVAL_TIME",
        	"MODEL",
        	"TICKET",
        	"COST",
        	"FLIGHT_DATE",
        	"CRAWL_DATE")
            VALUES(
            "%s","%s","%s","%s","%s","%s",
            "%s","%s","%s","%s","%d","%s","%s");
            '''%(row['id'],row['aviation'],row['flight'],row['route'],row['departure'],row['arrival'],row['departure_time'],row['arrival_time'],row['model'],row['ticket'],row['cost'],row['flight_date'],row['crawl_date'])
        SQLite_cursor.execute(insertSQLtoSQLite)
        
        return SQLite_cursor 

SQLite_connection = sqlite3.connect('S0016698978.db')
SQLite_cursor=SQLite_connection.cursor()
SQLite_cursor.execute("begin")


#fat-fare_data_1518019200 遠東航空
#ma-fare_data_1518019200 華信航空
#ua-fare_data_1518019200 立榮航空
#華信航空的cost型別存成string
fatfare_data='fat-fare_data_1519142400'
mafare_data='ma-fare_data_1519142400'
uafare_data='ua-fare_data_1519142400'
AviationList=[fatfare_data,mafare_data,uafare_data]

for Aviation in AviationList:

    consumer = KafkaConsumer(Aviation,auto_offset_reset='earliest',enable_auto_commit=False,bootstrap_servers=['192.168.66.121:9092'],consumer_timeout_ms=3000)
    print ("Waiting for messages...")
    print(Aviation)
    
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset,message.key,message.value))
        row=json.loads(message.value.decode(encoding="utf-8", errors="strict"))
        row['cost']=toint(row['cost'])
        print(row)
        SQLite_cursor = (insertDictSQL(row))
        
    #一個航空完成後聆聽三秒無訊息繼續下一個航空
    consumer.close()

SQLite_cursor.execute("commit")    
SQLite_cursor.close()

SQLite_connection.close()
    


