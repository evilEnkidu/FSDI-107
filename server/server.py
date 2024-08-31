from flask import Flask 
import json
app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name" : "Emil"}
    return json.dumps(me)

@app.get("/footer") #this section is NOT a page
def footer():
    pageName = {"pageName" : "Organika"}
    return json.dumps(pageName)

app.run(debug=True)

