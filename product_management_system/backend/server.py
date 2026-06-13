from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.sql_connection import get_sql_connection

from backend import products_dao
from backend import orders_dao
from backend import uom_dao
from backend import auth_dao

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="../ui"
)
CORS(app)

# ---------------------------
# SAFE DB CONNECTION
# ---------------------------
def get_connection():
    return get_sql_connection()


# ---------------------------
# HOME
# ---------------------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------------------
# UOM API
# ---------------------------
@app.route('/getUOM', methods=['GET'])
def get_uom():
    conn = get_connection()
    try:
        response = uom_dao.get_uoms(conn)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# PRODUCTS API
# ---------------------------
@app.route('/getProducts', methods=['GET'])
def get_products():
    conn = get_connection()
    try:
        response = products_dao.get_all_products(conn)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    conn = get_connection()

    try:
        request_payload = request.get_json()

        if not request_payload:
            return jsonify({"error": "No data received"}), 400

        product_id = products_dao.insert_new_product(conn, request_payload)

        return jsonify({'product_id': product_id})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    conn = get_connection()

    try:
        data = request.get_json()

        if not data or 'product_id' not in data:
            return jsonify({"error": "product_id missing"}), 400

        return_id = products_dao.delete_product(conn, data['product_id'])

        return jsonify({'product_id': return_id})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# ORDERS API
# ---------------------------
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    conn = get_connection()

    try:
        response = orders_dao.get_all_orders(conn)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    conn = get_connection()

    try:
        request_payload = request.get_json()

        if not request_payload:
            return jsonify({"error": "No data received"}), 400

        if 'customer_name' not in request_payload or 'total' not in request_payload:
            return jsonify({
                "error": "Missing required fields",
                "received": request_payload
            }), 400

        order_id = orders_dao.insert_order(conn, request_payload)

        return jsonify({'order_id': order_id})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():

    conn = get_connection()
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = auth_dao.login_user(conn, username, password)

    if not user:
        return jsonify({
            "error": "Invalid username or password"
        }), 401

    return jsonify({
        "user_id": user["user_id"],
        "username": user["username"],
        "role": user["role"]
    })

# ---------------------------
# RUN SERVER
# ---------------------------
import os

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)