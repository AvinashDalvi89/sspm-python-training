from flask import Flask, request, jsonify, make_response
import datetime
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

#this is to throw error which method is allow
@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Method Not found','status': 405}), 405)


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

    return jsonify(product_list)

@app.route('/product/<id>')
def get_product(id):
    product_sql = "select * from tbl_products where id = " + id + ""

    my_cursor.execute(product_sql)
    product_result = my_cursor.fetchone()
    column_list = ["id", "name", "category", "subCategory", "availableQuantity", "description",
                   "price", "brand"]
    print(product_result)
    product_dict = {}
    i = 0
    for product in product_result:
        if i < len(column_list):
            product_dict[column_list[i]] = product
            # print(product_dict)
            i = i + 1
    return jsonify(product_dict)


@app.route('/add/product', methods=['POST'])
def add_product():
    params = request.get_json()
    product_name = params.get('name')
    category = params.get('category')
    sub_category = params.get('subCategory')
    available_quantity = params.get('availableQuantity')
    description = params.get('description')
    price = params.get('price')
    brand = params.get('brand')
    image_url = params.get('imgUrl')
    today_date_time = datetime.datetime.now()
    today_date_time = today_date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(today_date_time)
    insert_product_sql = "INSERT INTO tbl_products(product_name,category,sub_category,available_qty," \
             "description,price,brand_name,img_url,created_at,modified_at,created_by," \
             "modified_by) VALUES (%s, %s, %s, %s,%s, %s,%s, %s, %s, %s,1,1)"
    insert_value = (product_name, category, sub_category, available_quantity, description, price, brand,image_url,
                    today_date_time,today_date_time)
    my_cursor.execute(insert_product_sql, insert_value)

    my_db.commit()
    if my_cursor.rowcount > 0:
        return {"status": "Successfully added product"}
    else:
        return {"status": "Error in adding product"}


@app.route('/update/product/<id>', methods=['POST'])
def update_product(id):
    params = request.get_json()
    product_name = params.get('name')
    category = params.get('category')
    sub_category = params.get('subCategory')
    available_quantity = params.get('availableQuantity')
    description = params.get('description')
    price = params.get('price')
    brand = params.get('brand')
    image_url = params.get('imgUrl')
    today_date_time = datetime.datetime.now()
    today_date_time = today_date_time.strftime("%Y-%m-%d %H:%M:%S")
    #print(today_date_time)
    update_sql = "UPDATE tbl_products SET modified_at = '" +today_date_time+"', modified_by = 2, " \
                                                                          "price = "+ str(price) + " WHERE id = "+ str(id)+ ""

    my_cursor.execute(update_sql)

    my_db.commit()
    if my_cursor.rowcount > 0:
        return {"status": "Successfully updated product"}
    else:
        return {"status": "Error in updating product"}

@app.route('/delete/product/<id>', methods=['POST'])
def delete_product(id):
    
    #print(today_date_time)
    update_sql = "DELETE FROM tbl_products WHERE id = " + str(id)+""

    my_cursor.execute(update_sql)

    my_db.commit()
    if my_cursor.rowcount > 0:
        return {"status": "Successfully deleted product"}
    else:
        return {"status": "Error in deleting product"}


@app.route('/add/cart', methods=['POST'])
def add_to_cart():
    params = request.get_json()
    product_id = params.get('product_id')
    quantity = params.get('quantity')
    get_product_sql = "select * from tbl_products where id = " + str(product_id) + ""
    my_cursor.execute(get_product_sql)
    product_result = my_cursor.fetchone()
    column_list = ["id", "name", "category", "subCategory", "availableQuantity", "description",
                   "price", "brand"]
    product_dict = {}
    i = 0
    for product in product_result:
        if i < len(column_list):
            product_dict[column_list[i]] = product
            # print(product_dict)
            i = i + 1

    cart_price = quantity * product_dict['price']
    shipping_charges = (1 * cart_price)/100
    total_cart_price = cart_price + shipping_charges
    today_date_time = datetime.datetime.now()
    today_date_time = today_date_time.strftime("%Y-%m-%d %H:%M:%S")
    insert_sql = "INSERT INTO tbl_carts(product_id,quantity, cart_value,shipping_charges,total_cart_value,created_at,modified_at,created_by," \
                 "modified_by) VALUES (%s, %s,%s, %s,%s, %s,%s,1,1)"

    insert_val = (product_id,quantity,cart_price,shipping_charges,total_cart_price,today_date_time,today_date_time)
    my_cursor.execute(insert_sql, insert_val)
    my_db.commit()
    if my_cursor.rowcount > 0:
        return {"status": "Successfully added product to cart"}
    else:
        return {"status": "Error in adding product to cart"}

