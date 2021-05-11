import mysql.connector


class DB:

    def __init__(self):

        self.my_db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="ecommerce_site"
        )
        self.my_cursor = self.my_db.cursor()





