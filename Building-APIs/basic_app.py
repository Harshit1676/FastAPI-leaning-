from fastapi import FastAPI

app = FastAPI()

@app.get('/')    # decorater
def home():
    return {"message":"Hello, FastAPI!"}

