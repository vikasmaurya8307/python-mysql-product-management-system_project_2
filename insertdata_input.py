from database import conn,pool
import pandas as pd
import os 
os.system("cls")

try : 
    products_id = int(input("enter a product id : "))
    products_name = str(input("enter a product name : "))
    products_price  = int(input("enter a product price : "))
    sql = '''insert  into products(products_id,products_name,products_price)
    values(%s,%s,%s)
'''
 
    pool.execute(sql,(products_id,products_name,products_price))
    conn.commit()
    print("done")

except Exception as err :
    print(f"error : {err}")