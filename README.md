# python-mysql-product-management-system
CLI-based Product Management System using Python, MySQL, and Pandas to insert, display, and search product records with structured tabular output.
🗄️ Product Database Management System (Python + MySQL)

A simple command-line based project built using Python, MySQL, and Pandas to manage product data.
This project allows you to connect to a database, insert product records, and search products by ID.

📌 Features

✔ Connect to MySQL database
✔ Insert new product records
✔ View all product records
✔ Search product by ID
✔ Display results in table format using Pandas

🛠️ Technologies Used

Python 3.x

MySQL Server

mysql-connector-python

pandas

📁 Project Structure
📦 project-folder
 ┣ 📜 database.py            # Database connection file
 ┣ 📜 insertdata_input.py    # Insert new product data
 ┣ 📜 searching.py           # View & search products
 ┗ 📜 README.md              # Project documentation
⚙️ Database Setup

Open MySQL and run the following SQL:

CREATE DATABASE indian_bank;

USE indian_bank;

CREATE TABLE products (
    products_id INT PRIMARY KEY,
    products_name VARCHAR(50),
    products_price INT
);
🔌 Database Connection Config

Update your credentials inside database.py:

config1 = {
    "host": "localhost",
    "user": "root",
    "port": 3306,
    "password": "",
    "database": "indian_bank",
}
▶️ How to Run the Project
1️⃣ Install dependencies
pip install mysql-connector-python pandas
2️⃣ Run Database Connection
python database.py

You should see:

db connect successfully
3️⃣ Insert Product Data
python insertdata_input.py

Example input:

enter a product id : 101
enter a product name : Laptop
enter a product price : 50000
4️⃣ View & Search Product
python searching.py

✔ Shows all products
✔ Asks for product ID
✔ Displays result in table format

📊 Example Output
======================All Products=======================
   products_id products_name products_price
0          101        Laptop          50000
=========================================================

Enter product_id to search: 101

Searching --------------
Product Found

   products_id products_name products_price
0          101        Laptop          50000
