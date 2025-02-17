from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            },
            {
                "name": "Bed",
                "price": 120.23
            }
        ]
    }
]


@app.get('/stores')
def get_stores():
    return {"stores": stores}, 200


@app.post('/stores')
def create_store():
    data = request.get_json()
    new_store = {"name": data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post('/stores/<string:name>/item')
def create_item(name):
    data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": data["name"], "price": data["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "Store not found"}, 404
