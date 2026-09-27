from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"Hola! Esta es una aplicacion FastAPI corriendo en Docker"}