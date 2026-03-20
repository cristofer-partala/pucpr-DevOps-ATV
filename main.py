from fastapi import FastAPI

app = FastAPI(title="API de Monitoramento de Rede")

@app.get("/")
def read_root():
    return {"mensagem": "API de monitoramento de rede em execução"}

@app.get("/teste")
async def funcao_teste():
    return {"mensagem": "Rota de teste funcionando"}

@app.get("/status")
def status():
    return {"status": "online"}
