from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flask World!😃"

@app.route("/get-products")
def get_products():
    return {
        "name": "SSPM",
        "pincode": 453053,
        "id" : 1
    }