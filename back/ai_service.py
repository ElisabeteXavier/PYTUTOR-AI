
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
from back.config import OPENAI_API_KEY
from back.prompts import PROMPT_A, PROMPT_B
from back.metrics import calcular_perplexidade, calcular_bleu


class Pergunta(BaseModel):
    pergunta: str

client = OpenAI(api_key=OPENAI_API_KEY)

REFERENCIAS = {
    "lista": """
    Uma lista em Python é uma estrutura de dados mutável que armazena elementos de forma ordenada.
    Pode conter diferentes tipos de dados e permite operações como inserção, remoção e acesso por índice.
    """,

    "dicionario": """
    Um dicionário em Python é uma coleção de pares chave-valor, onde cada chave é única.
    Ele permite acesso rápido aos valores através de suas chaves.
    """,

    "tupla": """
    Uma tupla em Python é uma coleção ordenada e imutável de elementos.
    Diferente das listas, não permite alteração após a criação.
    """,

    "função": """
    Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica.
    Ela pode receber parâmetros e retornar valores.
    """
}

def processar_pergunta(pergunta: str):

    resp_a = gerar_resposta(PROMPT_A, pergunta)
    resp_b = gerar_resposta(PROMPT_B, pergunta)

    referencia = buscar_referencia(pergunta)

    perplexidade_a = calcular_perplexidade(resp_a)
    perplexidade_b = calcular_perplexidade(resp_b)

    bleu_a = calcular_bleu(resp_a, referencia)
    bleu_b = calcular_bleu(resp_b, referencia)

    return {
        "resposta_A": resp_a,
        "resposta_B": resp_b,
        "metricas": {
            "perplexidade_A": perplexidade_a,
            "perplexidade_B": perplexidade_b,
            "bleu_A": bleu_a,
            "bleu_B": bleu_b
        }
    }

def gerar_resposta(prompt, pergunta):
    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",  # rápido e mais barato
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": pergunta}
        ],
        temperature=0.7,
        max_tokens=200
    )

    return resposta.choices[0].message.content

def buscar_referencia(pergunta: str):
    pergunta_lower = pergunta.lower()

    for tema, referencia in REFERENCIAS.items():
        if tema in pergunta_lower:
            return referencia

    return "Referência não encontrada para esse tema."