from flask import Flask, request, jsonify, make_response
import mysql.connector
my_db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="ecommerce_site"
        )
my_cursor = my_db.cursor()

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route("/")
def hello():
    return "Welcome to Flask World!😃"

@app.route("/get-products")
def get_products():
    sql = "select * from tbl_products "
    my_cursor.execute(sql)

    product_result = my_cursor.fetchall()
    print(product_result)
    product_list = []
    column_list = ["id","name","category","subCategory","availableQuantity","description","price","brand","imageUrl"]
    for product_details in product_result:
        print(product_details)
        i = 0
        product_dict = {}
        for product in product_details:
            if i < len(column_list):

                product_dict[column_list[i]] = product
                #print(product_dict)
                i = i + 1

        product_list.append(product_dict)

    # return {
    #       "id": 1,
    #       "name": 'T-shirt',
    #       "category": 'Clothing',
    #       "subCategory": 'TShirt',
    #       "availableQuantity": 100,
    #       "description": 'Half Sleeve T-shirt',
    #       "price": 100,
    #       "brand": 'Puma',
    #       "imageUrl": 'http://image.url',
    # }
    return jsonify(product_list)