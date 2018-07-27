#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:01:01 2018

@author: mingcheien
"""

import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()
SQL='''CREATE TABLE company123(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL
);'''
c.execute(SQL)
#print ('table create successfully')

insertSQL="insert into company (ID,NAME,AGE) values  (3,'Kelly',20);"
#c.execute(insertSQL)

selectSQL="select * from company where age=18 ;"

selectList = c.execute(selectSQL)
for row in selectList:
    print (row[0])
    print (row[1])
    print (row[2])
conn.commit()
conn.close()