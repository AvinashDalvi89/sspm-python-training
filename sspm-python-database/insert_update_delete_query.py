import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ecommerce_site"
)

my_cursor = my_db.cursor()

# inserting of record into table
insert_sql = "INSERT INTO tbl_products(product_name,category,sub_category,available_qty," \
             "description,price,brand_name,img_url,created_at,modified_at,created_by," \
             "modified_by) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"

insert_val = ("Green Shirt 1", "Clothing", "Shirt", 230,"This best shirt ", 130, "Peter England", "https://ibb.co/WttCg1v",
              "2021-05-10 10:330:30", "2021-05-10 10:330:30", 1,1)
my_cursor.execute(insert_sql, insert_val)

my_db.commit()

print(my_cursor.rowcount, "record inserted.")

# updation of record into table
update_sql = "UPDATE tbl_products SET price = 300 WHERE product_name = 'Green Shirt'"

my_cursor.execute(update_sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) affected")


# deletion of record from table

delete_sql = "DELETE FROM tbl_products WHERE product_name = 'Green Shirt 1'"

my_cursor.execute(delete_sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) deleted")

