from urllib import response
from flask import Flask, jsonify, request
from database import delete_product, get_product, create_product
from sql_connection import get_sql_connection
from flask_cors import CORS

cnx = get_sql_connection()

app = Flask(__name__)
CORS(app)

@app.route("/getProducts", methods=['GET'])
def getProducts():
   try:
      response = get_product(cnx)
      if response['status'] == "success":
         return jsonify({"message": "Product fetched successfully!", "data":response['data']}), 200
      else:
         return jsonify({"message":"Error while fetching product"}), 400
   except:
      return jsonify({"message":"Error while fetching product"}), 400

@app.route("/deleteProduct",methods=['POST'])
def deleteProduct():
   try:
      product_id = request.get_json()
      response = delete_product(cnx, product_id['product_id'])
      if response['status'] == "success":
         return jsonify({"message": "Product deleted successfully!"}), 200
      else:
         return jsonify({"message":"Error while deleting product"}), 400
   except:
      return jsonify({"message":"Error while deleting product"}), 400

@app.route("/createProduct",methods=['POST'])
def createProduct():
   try:
      product = request.get_json()
      response = create_product(cnx,product)
      if response['status'] == "success":
         return jsonify({"message": "Product added successfully!"}), 200
      else:
         return jsonify({"message":"Error while adding product"}), 400
   except:
      return jsonify({"message":"Error while adding product"}), 400

@app.route("/updateProduct",methods=['POST'])
def updateProduct():
   try:
      product = request.get_json()
      response = create_product(cnx,product)
      if response['status'] == "success":
         return jsonify({"message": "Product added successfully!"}), 200
      else:
         return jsonify({"message":"Error while adding product"}), 400
   except:
      return jsonify({"message":"Error while adding product"}), 400

if __name__ == '__main__':
    app.run(debug=True)