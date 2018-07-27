#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:05:01 2018

@author: mingcheien
"""

from flask import Flask 
from flask import url_for
from flask import render_template
from flask import request
import pandas as pd
import json

app = Flask(__name__)
@app.route("/")

def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
@app.route('/auth',methods=['POST'])

def authAccount():
    
    with open ('accountInformation.json') as f :
        accountjson=json.load(f)
        accountList=accountjson['account']
        passwordList=accountjson['password']
        
        for account in accountList :
            if accountList[account] ==request.form['account'] and passwordList[account]==request.form['']:
                return 'you got it'
            else:
                return request.form['account']

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

with app.test_request_context():
        print (url_for('index'))
        #print url_for('login')
        #print url_for('login', next='/')
        #print url_for('profile', username='John Doe')

'''
app.run最下面
'''
if __name__ == "__main__":
    app.run(debug=True)    
    