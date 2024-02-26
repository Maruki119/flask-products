from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo.mongo_client import MongoClient

#add mongodb to api
uri = "mongodb+srv://viewer:viewer@flask-products.vwhu75h.mongodb.net/?retryWrites=true&w=majority&appName=flask-products"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["flask-products"]
    products_collection = db["products"]
except Exception as e:
    print(e)
 
#main app
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

products=[
{"id":0,"name":"Notebook Acer Swift","price":45900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
{"id":1,"name":"Notebook Asus Vivo","price":19900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
{"id":2,"name":"Notebook Lenovo Ideapad","price":32900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
{"id":3,"name":"Notebook MSI Prestige","price":54900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
{"id":4,"name":"Notebook DELL XPS","price":99900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
{"id":5,"name":"Notebook HP Envy","price":46900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}]

@app.route("/")
def greet():
    return "<p>Welcome to Product API Management</p>"

@app.route("/products", methods=["GET"])
def get_all_products():
    return jsonify(products), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)