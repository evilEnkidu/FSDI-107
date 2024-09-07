from flask import Flask, request
import json
from config import dataBase

app = Flask(__name__)

product_list = []  # Assuming this might be a temporary fallback
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
    # Retrieve products from database
    products = list(dataBase.product_list.find())
    return json.dumps([fix_id(product) for product in products])

@app.get("/api/product/count")
def get_product_count():
    # Return the count of products in the database
    count = dataBase.product_list.count_documents({})
    return json.dumps({"count": count})

@app.post("/api/products")
def save_products():
    item = request.get_json()
    dataBase.product_list.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0 <= index < len(product_list):
        product_list[index] = update_item
        return json.dumps(update_item)
    else:
        return "That index doesn't exist", 404

if __name__ == "__main__":
    app.run(debug=True)
