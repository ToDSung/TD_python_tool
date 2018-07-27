#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:59:35 2018

@author: mingcheien
"""

import sqlite3

conn = sqlite3.connect('S0016698978.db')
c=conn.cursor()


SQL='''CREATE TABLE CROWDINSIGHT_AIRLINE_INFO(
    ID STRING(150) PRIMARY KEY NOT NULL,
    AVIATION STRING(30) NOT NULL,
    FLIGHT STRING(30) NOT NULL,
    ROUTE STRING(50) NOT NULL,
    DEPARTURE STRING(30) NOT NULL,
    ARRIVAL STRING(30) NOT NULL,
    DEPARTURE_TIME STRING(10) NOT NULL,
    ARRIVAL_TIME STRING(10) NOT NULL,
    MODEL STRING(30),
    TICKET STRING(30) NOT NULL,
    COST INT,
    FLIGHT_DATE LONGDATE NOT NULL,
    CRAWL_DATE LONGDATE NOT NULL

);'''
c.execute(SQL)
#print ('table create successfully')


conn.commit()
conn.close()