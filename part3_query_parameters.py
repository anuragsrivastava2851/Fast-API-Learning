from fastapi import FastAPI
app = FastAPI()


@app.get("/users")
def get_users(name: str): # here name is a query parameter, it can be any string value that is passed in the URL. For example, if the URL is /users?name=John, then name will be John. If the URL is /users?name=Jane, then name will be Jane.
    return {"name": name}

    # query parameters are optional, so if the name parameter is not passed in the URL, then it will be None. For example, if the URL is /users, then name will be None.

# query parameters can also have default values, so if the name parameter is not passed in the URL, then it will take the default value. For example, if the URL is /users, then name will be "Guest". If the URL is /users?name=John, then name will be John.

@app.get("/person")
def get_person(name: str = None): # here default parameter value is None, so if the name parameter is not passed in the URL, then it will be None. For example, if the URL is /users, then name will be None. If the URL is /users?name=John, then name will be John.

    return {"name": name}
@app.get("/products")
def get_products(limit: int=10): # here default parameter value is 10...
    return {"limit": limit}

@app.get("/items")
def get_items(name: str = None, price: int = 0):      
   
    return {"name": name, "price": price}  # multiple query parameters.. 
"""here it shows multiple query parameters, name and price.
        If the URL is /items?name=Book&price=100, then name will be Book and price will be 100.
        If the URL is /items?name=Book, then name will be Book and price will be 0.
        If the URL is /items?price=100, then name will be None and price will be 100.
        If the URL is /items, then name will be None and price will be 0."""




## important examples

@app.get("/students")
def get_students(course: str):

    students = [
        {"id": 101, "name": "Anurag", "course": "CSE"},
        {"id": 102, "name": "Rahul", "course": "IT"},
        {"id": 103, "name": "Aman", "course": "CSE"},
        {"id": 104, "name": "Priya", "course": "ECE"}
    ]

    result = []

    for student in students:
        if student["course"] == course:
            result.append(student)

    return result

#uvicorn part3_query_parameters:app --reload
