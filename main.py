from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo com FastAPI!"}

@app.get("/teste")
async def funcaoteste():
    return {"mensagem": "TESTE com FastAPI!"}
@app.get("/status")
def status():
    return {"status": "online"}
def test_exemplo():
    assert 1 == 1
