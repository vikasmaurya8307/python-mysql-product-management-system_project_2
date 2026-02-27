from database import conn , pool    
import pandas as pd
import time
import os
os.system("cls")

try : 
    pool.execute("SELECT * FROM products")
    result = pool.fetchall()

    print("======================All Products======================= ")
    time.sleep(1)
    print(pd.DataFrame(result))

    print("=========================================================")
    products_id = int(input("Enter product_id to search: "))

    sql = "SELECT * FROM products WHERE products_id = %s"
    pool.execute(sql, (products_id,))
    result = pool.fetchall()
    print("Searching --------------")
    time.sleep(1)
 
    if result:
        print("Product Found")
    else:
        print("Product not found")
    
    print(pd.DataFrame(result))
    
 
except Exception as err :
    print(err)