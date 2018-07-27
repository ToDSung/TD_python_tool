#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:26:23 2018

@author: mingchien
"""
"""
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')
    print(_)
"""
from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer
import sys

kafka = KafkaClient('127.0.0.1:9092')
producer = KafkaProducer()

group_name = "my-group"
topic_name = "fast-message"
print ("sending messages to group: [%s] and topic: [%s]" % (group_name, topic_name))

# send only one message
producer.send('fast-message', value=b"Some message")