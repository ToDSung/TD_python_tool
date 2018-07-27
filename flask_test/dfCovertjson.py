#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:21:56 2018

@author: mingcheien
"""

import pandas as pd 
import json

dict={'account':['qwer1234','asdf5678'],'password':['qwer5678','asdf1234']}

df=pd.DataFrame(data=dict)
print(df)

df.to_json('accountInformation.json')



with open ('accountInformation.json') as f :
        accountjson=json.load(f)
        accountList=accountjson['account']
        passwordList=accountjson['password']
        
        for account in accountList :
            print (accountList[account])
            print(passwordList[account])