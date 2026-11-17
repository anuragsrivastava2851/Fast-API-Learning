from fastapi import FastAPI

app = FastAPI()

# home route
@app.get("/")
def home():
    return {"message": "Hello World"}



# about route
@app.get("/about")
def about():
    return {"message": "This is the about page"}


# users route
@app.get("/users")
def users():
    return {
        "message": ["User 1", "User 2", "User 3"]
            
    }