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
    """
    Retrieve a list of stores.

    This endpoint returns a JSON object containing a list of stores
    available in the system. The response includes a status code of 200
    indicating a successful request.

    Returns:
        dict: A dictionary containing a key 'stores' with the list of stores.
        int: HTTP status code 200.
    """
    return {"stores": stores}, 200


@app.post('/stores')
def create_store():
    """
    Create a new store.

    This endpoint receives a JSON payload containing the store's name,
    creates a new store object with an empty items list, and appends it
    to the stores list. It returns the newly created store object along
    with a 201 Created status code.

    Returns:
        tuple: A tuple containing the newly created store object and 
               the HTTP status code 201.
    """
    data = request.get_json()
    new_store = {"name": data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post('/stores/<string:name>/item')
def create_item(name):
    """
    Create a new item for a specified store.

    This endpoint receives a JSON payload containing the item's name and price.
    It searches for the store by the given name and, if found, creates a new item
    object and appends it to the store's items list. If the store is not found,
    it returns a 404 error message.

    Args:
        name (str): The name of the store where the item will be added.

    Returns:
        tuple: A tuple containing the newly created item object and 
               the HTTP status code 201 if successful, or a message 
               indicating the store was not found with a 404 status code.
    """
    # Get the JSON data from the request
    data = request.get_json()

    # Iterate through the list of stores to find the matching store by name
    for store in stores:
        if store["name"] == name:
            # Create a new item object with the provided name and price
            new_item = {"name": data["name"], "price": data["price"]}

            # Append the new item object to the store's items list
            store["items"].append(new_item)

            # Return the newly created item object and a 201 status code
            return new_item, 201

    # Return an error message if the store was not found
    return {"message": "Store not found"}, 404


@app.get('/stores/<string:name>')
def get_store(name):
    """
    Retrieve a store by its name.

    This endpoint searches for a store in the stores list by the given name.
    If the store is found, it returns the store object along with a 200 OK status code.
    If the store is not found, it returns a message indicating that the store was not found
    along with a 404 Not Found status code.

    Args:
        name (str): The name of the store to retrieve.

    Returns:
        tuple: A tuple containing either the store object and the HTTP status code 200
               if successful, or a message indicating the store was not found with a 
               404 status code.
    """
    # Iterate through the list of stores to find the matching store by name
    for store in stores:
        if store["name"] == name:
            # Return the found store object and a 200 status code
            return {"store": store}, 200

    # Return an error message if the store was not found
    return {"message": "Store not found"}, 404


@app.get('/stores/<string:name>/item')
def get_store_item(name):
    """
    Retrieve the items available in a specific store.

    Args:
        name (str): The name of the store for which to retrieve items.

    Returns:
        dict: A dictionary containing the list of items in the store if found.
        dict: A message indicating that the store was not found, along with a 404 status code.
    """
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}

    return {"message": "Store not found"}, 404
