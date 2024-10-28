from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {"name": "table", "price": 5000}
        ]
    }
]

def find_store(name):
    return next((store for store in stores if store["name"] == name), None)

@app.get("/store")
def get_all_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    if not request_data or "name" not in request_data:
        return {"message": "Store name is required"}, 400

    if find_store(request_data["name"]):
        return {"message": "Store already exists"}, 400

    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    store = find_store(name)
    if not store:
        return {"message": "Store not found"}, 404

    request_data = request.get_json()
    if "name" not in request_data or "price" not in request_data:
        return {"message": "Item name and price are required"}, 400
    if not isinstance(request_data["price"], (int, float)):
        return {"message": "Price should be a number"}, 400

    new_item = {"name": request_data["name"], "price": request_data["price"]}
    store["items"].append(new_item)
    return new_item, 201

@app.get("/store/<string:name>")
def get_single_store(name):
    store = find_store(name)
    if store:
        return store
    return {"message": "No such store found"}, 404

@app.get("/store/<string:storename>/<string:itemname>")
def get_single_item(storename, itemname):
    store = find_store(storename)
    if store:
        item = next((item for item in store["items"] if item["name"] == itemname), None)
        if item:
            return item
    return {"message": "No such store/item found"}, 404
