from flask import Flask, jsonify
from database import get_all_product
from sql_connection import get_sql_connection 

cnx = get_sql_connection()

app = Flask(__name__)

@app.route("/getProducts", methods=['GET'])
def getProducts():
   products = get_all_product(cnx)
   response = jsonify(products)
   response.headers.add('Access-Control-Allow-Origin','*')
   return response

if __name__ == '__main__':
    app.run(debug=True)