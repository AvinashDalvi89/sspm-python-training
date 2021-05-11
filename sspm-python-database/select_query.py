import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ecommerce_site"
)

my_cursor = my_db.cursor()

sql = "select * from tbl_products "
my_cursor.execute(sql)

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)