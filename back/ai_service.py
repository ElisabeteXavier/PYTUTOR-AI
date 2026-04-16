
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
from config import OPENAI_API_KEY


class Pergunta(BaseModel):
    pergunta: str

client = OpenAI(api_key=OPENAI_API_KEY)

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