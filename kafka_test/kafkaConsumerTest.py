#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:32:15 2018

@author: mingchien
"""

from kafka import SimpleConsumer, SimpleClient
from kafka import KafkaConsumer
from kafka import KafkaClient


group_name = "my-group"
topic_name = "fast-message"
'''
bootstrap_servers = '192.168.67.39:9092'
kafka = KafkaClient('127.0.0.1:9092')
consumer = KafkaConsumer(topic_name,group_id=group_name)

for msg in consumer:
    print (msg)
'''

consumer = KafkaConsumer('fat-fare_data_1517932800',auto_offset_reset='earliest',enable_auto_commit=False,bootstrap_servers=['192.168.67.39:9092'])
print ("Created consumer for group: [%s] and topic: [%s]" % (group_name, topic_name))
print ("Waiting for messages...")
for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset,message.key,message.value))
    print(message.value.decode(encoding="utf-8", errors="strict"))
