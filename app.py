from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("products.json") as f:
        products = json.load(f)
    return render_template("index.html", products=products)

@app.route("/product/<int:pid>")
def product(pid):
    with open("products.json") as f:
        products = json.load(f)
    product = next((p for p in products if p["id"] == pid), None)
    return render_template("product.html", product=product)

@app.route("/api/products")
def api_products():
    with open("products.json") as f:
        products = json.load(f)
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
