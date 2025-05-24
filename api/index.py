from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Student Marks API!"}

@app.get("/api")
def get_example():
    return {"example": "This is where student marks will be retrieved."}
