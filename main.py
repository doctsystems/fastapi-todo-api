from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"mesaje": "Hello Wolrd from FastAPI :)"}
