from fastapi import FastAPI

app = FastAPI(title="API de Monitoramento de Rede")

@app.get("/info")
def info():
    return {"app": "monitoramento", "versao": "1.0"}

@app.get("/teste")
async def funcao_teste():
    return {"mensagem": "Rota de teste funcionando"}

@app.get("/status")
def status():
    return {"mensagem": "API de monitoramento online"}
