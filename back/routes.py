from fastapi import APIRouter
from back.ai_service import processar_pergunta, Pergunta

routes = APIRouter(prefix ="/chat",tags=["chat"])

@routes.post("/ask")
async def perguntar(data: Pergunta):
    resultado = processar_pergunta(data.pergunta)

    return {
        "pergunta": data.pergunta,
        **resultado
    }
