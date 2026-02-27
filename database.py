import mysql.connector
import pandas as pd


config1 = {
    "host": "localhost",
    "user" : "root",
    "port" : 3306,
    "password" : "",
    "database" : "indian_bank",
    }
    
try : 
    conn = mysql.connector.connect(**config1)
    pool = conn.cursor(dictionary=True)
    print(f"db connect succesfully")
except Exception as err :
    print(f" error is : {err}")