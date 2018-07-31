import logging
import pymysql 
import psycopg2 
import pyodbc 
import cx_Oracle


def conn_postgre(input_host, input_port=5432, input_username, input_password):
    postgre_conn = psycopg2.connect(
        host=input_host, port=input_port, user=input_username, password=input_password)
    return postgre_conn
    
    #postgre_cursor = postgre_conn.cursor()
    #postgre_cursor.execute("SELECT VERSION()")
    #postgre_db_version = postgre_cursor.fetchone()
    #print(postgre_db_version)
    #postgre_cursor.close()
    #postgre_conn.close()


def conn_maria(input_host, input_port=3306, input_username, input_password):
    maria_conn = pymysql.connect(host=input_host, port=input_port,
                                 user=input_username, password=input_password, charset='utf8')
    return maria_conn
    
    #maria_cursor = maria_conn.cursor()   
    #maria_cursor.execute("SELECT VERSION()") 
    #maria_db_version = maria_cursor.fetchone() 
    #print(maria_db_version) 
    #maria_cursor.close() 
    #maria_conn.close() 


def conn_mssql(input_host, input_port=1433, input_username, input_password):

    server = ','.join(input_host,input_port)
    #server = '192.168.66.67,10003' 
    username = input_username
    password = input_password
    mssql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
    
    return mssql_conn

    #mssql_cursor = mssql_conn.cursor()
    #mssql_cursor.execute("SELECT @@VERSION")
    #mssql_db_version = mssql_cursor.fetchone()
    #print(mssql_db_version)
    #mssql_cursor.close()
    #mssql_conn.close()    
