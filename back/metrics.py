# nlp_metrics.py

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# carregar modelo UMA VEZ (importantíssimo)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

smoothie = SmoothingFunction().method4


# 🔥 PERPLEXIDADE REAL
def calcular_perplexidade(texto):
    inputs = tokenizer(texto, return_tensors='pt')

    with torch.no_grad():
        outputs = model(**inputs, labels=inputs['input_ids'])
        loss = outputs.loss

    perplexidade = torch.exp(loss)
    return perplexidade.item()


# 🔥 BLEU REAL
def calcular_bleu(resposta, referencia):
    return sentence_bleu(
        [referencia.split()],
        resposta.split(),
        smoothing_function=smoothie
    )