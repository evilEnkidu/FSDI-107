from flask import Flask, request
import json
from config import dataBase

app = Flask(__name__)

product_list = []  # Renamed to avoid the name conflict
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

@app.get("/footer")  # This section is NOT a page
def footer():
    pageName = {"pageName": "Organika"}
    return json.dumps(pageName)

@app.get("/api/products")
def get_products():  # Renamed to avoid the name conflict
    return json.dumps(product_list)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    #product_list.append(item)
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
        return "That index doesn't exist"



if __name__ == "__main__":
    app.run(debug=True)
