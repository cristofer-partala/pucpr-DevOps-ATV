from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo com FastAPI!"}

@app.get("/teste")
async def funcaoteste():
    return {"mensagem": "TESTE com FastAPI!"}
