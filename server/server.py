from flask import Flask, request
import json
from config import dataBase  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name": "Emil"}
    return json.dumps(me)

@app.get("/footer")
def footer():
    pageName = {"pageName": "Organika"}
    return json.dumps(pageName)

@app.get("/api/products")
def get_products():
    # Retrieve products from the database
    productsCursor = list(dataBase.catalog.find({}))
    return json.dumps([fix_id(product) for product in productsCursor])

@app.get("/api/product/count")
def get_product_count():
    # Return the count of products in the database
    count = dataBase.product_list.count_documents({})
    return json.dumps({"count": count})

@app.post("/api/products")
def save_products():
    item = request.get_json()
    dataBase.catalog.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    # You don't need to update the local product_list unless you're using it elsewhere
    return json.dumps(update_item)


# Post new Coupon 
@app.post("/api/coupons")
def save_coupon():
    new_coupon = request.get_json()
    dataBase.coupons.insert_one(new_coupon)
    print(new_coupon)
    return json.dumps(fix_id(new_coupon))


# Retrieve coupons from the database
@app.get("/api/coupons")
def get_coupons():
    couponsCursor = list(dataBase.coupons.find({}))
    return json.dumps([fix_id(coupon) for coupon in couponsCursor])

if __name__ == "__main__":
    app.run(debug=True)
