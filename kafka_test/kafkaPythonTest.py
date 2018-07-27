#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:26:23 2018

@author: mingchien
"""

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')
    print(_)