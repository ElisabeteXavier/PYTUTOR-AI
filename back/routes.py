from fastapi import APIRouter
from back.prompts import PROMPT_A, PROMPT_B
from back.ai_service import gerar_resposta, Pergunta
from back.metrics import calcular_perplexidade, calcular_bleu

routes = APIRouter(prefix ="/chat",tags=["chat"])

@routes.post("/ask")
async def perguntar(data: Pergunta):
    pergunta = data.pergunta

    # respostas A/B
    resp_a = gerar_resposta(PROMPT_A, pergunta)
    resp_b = gerar_resposta(PROMPT_B, pergunta)

    #REFERÊNCIA (simples por enquanto)
    referencia = "Uma lista em Python é uma coleção de elementos."

    # MÉTRICAS REAIS
    perplexidade_a = calcular_perplexidade(resp_a)
    perplexidade_b = calcular_perplexidade(resp_b)

    bleu_a = calcular_bleu(resp_a, referencia)
    bleu_b = calcular_bleu(resp_b, referencia)

    return {
        "pergunta": pergunta,
        "resposta_A": resp_a,
        "resposta_B": resp_b,
        "metricas": {
            "perplexidade_A": perplexidade_a,
            "perplexidade_B": perplexidade_b,
            "bleu_A": bleu_a,
            "bleu_B": bleu_b
        }
    }