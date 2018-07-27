import logging
import pymysql 
import psycopg2 
import pyodbc 
import cx_Oracle

def conn_postgre():
    postgre_conn = psycopg2.connect(host='192.168.66.67', port=10001, user='username',password='ciPs1618')
    return postgre_conn
    
    #postgre_cursor = postgre_conn.cursor()
    #postgre_cursor.execute("SELECT VERSION()")
    #postgre_db_version = postgre_cursor.fetchone()
    #print(postgre_db_version)
    #postgre_cursor.close()
    #postgre_conn.close()
def conn_maria(): 
    maria_conn = pymysql.connect(host='192.168.66.67', port=10002, user='username',password='ciPs1618',charset='utf8') 
    return maria_conn
    
    #maria_cursor = maria_conn.cursor()   
    #maria_cursor.execute("SELECT VERSION()") 
    #maria_db_version = maria_cursor.fetchone() 
    #print(maria_db_version) 
    #maria_cursor.close() 
    #maria_conn.close() 
def conn_mssql():

    server = '192.168.66.67,10003' 
    username = 'sa' 
    password = 'ciPs1618' 
    mssql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
    
    return mssql_conn

    #mssql_cursor = mssql_conn.cursor()
    #mssql_cursor.execute("SELECT @@VERSION")
    #mssql_db_version = mssql_cursor.fetchone()
    #print(mssql_db_version)
    #mssql_cursor.close()
    #mssql_conn.close()    