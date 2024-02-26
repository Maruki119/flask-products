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

#products=[
#{"id":0,"name":"Notebook Acer Swift","price":45900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
#{"id":1,"name":"Notebook Asus Vivo","price":19900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
#{"id":2,"name":"Notebook Lenovo Ideapad","price":32900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
#{"id":3,"name":"Notebook MSI Prestige","price":54900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
#{"id":4,"name":"Notebook DELL XPS","price":99900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
#{"id":5,"name":"Notebook HP Envy","price":46900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}]

@app.route("/")
def greet():
    return "<p>Welcome to Product API Management</p>"

@app.route("/products", methods=["GET"])
def get_all_products():
    try:
        all_products = list(products_collection.find())
        return jsonify(all_products)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/products/<int:prod_id>", methods = ["GET"])
def get_product_id(prod_id):
    try:
        product = products_collection.find_one({"_id": prod_id})
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/products", methods = ["POST"])
def add_product():
    try:
        data = request.get_json()
        already_data = products_collection.find_one({"_id": data.get("_id")})
        if(already_data):
            return jsonify({"error":"Cannot create product"})
        products_collection.insert_one(data)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/products/<int:prod_id>", methods = {"PUT"})
def update_product(prod_id):
    try:
        data = request.get_json()
        product_data = products_collection.find_one({"_id": prod_id})
        if not product_data:
            return jsonify({"error": "Prodecut not found"}), 404
        products_collection.update_one({"_id": prod_id}, {"$set": data})
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/products/<int:prod_id>", methods = ["DELETE"])
def delete_product(prod_id):
    try:
        product_data = products_collection.find_one({"_id": prod_id})
        if not product_data:
            return jsonify({"error": "Product not found"}), 404
        products_collection.delete_one({"_id": prod_id})
        return jsonify({"message": "Product deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)