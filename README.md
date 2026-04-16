# PyTutor AI 🤖

Projeto desenvolvido como atividade prática do **3º módulo da Pós-Graduação em IA para Devs**, com foco em avaliação de respostas de modelos de linguagem utilizando métricas de NLP.

## 📌 Sobre o Projeto

O PyTutor AI é um tutor de Python baseado em IA que realiza **testes A/B de prompts**: para cada pergunta do usuário, dois perfis de tutor respondem simultaneamente — um teórico e um prático — e as respostas são avaliadas automaticamente com métricas de qualidade.

O objetivo é entender como diferentes estratégias de prompt afetam a qualidade das respostas geradas por LLMs.

## ⚙️ Métricas Utilizadas

| Métrica | O que mede |
|---|---|
| **Perplexidade** | Quão "surpreso" o modelo GPT-2 fica com o texto — quanto menor, mais fluente e coerente |
| **BLEU Score** | Similaridade entre a resposta gerada e uma referência — quanto maior, mais próxima do esperado |

## 🧪 Prompts A/B

- **Prompt A — Teórico:** tutor formal, com precisão técnica e definições completas
- **Prompt B — Prático:** tutor didático, com exemplos e linguagem simples

## 🛠️ Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — API REST do backend
- [OpenAI API](https://platform.openai.com/) — modelo `gpt-4.1-mini` para geração de respostas
- [Streamlit](https://streamlit.io/) — interface web do frontend
- [Transformers + GPT-2](https://huggingface.co/gpt2) — cálculo de perplexidade
- [NLTK](https://www.nltk.org/) — cálculo do BLEU Score

## 📁 Estrutura do Projeto

```
PyTutor AI/
├── back/
│   ├── main.py          # inicialização do FastAPI
│   ├── routes.py        # endpoint /chat/ask
│   ├── ai_service.py    # integração com a OpenAI
│   ├── prompts.py       # definição dos prompts A e B
│   └── metrics.py       # cálculo de perplexidade e BLEU
├── front/
│   └── app.py           # interface Streamlit
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Como Rodar

**1. Clone o repositório e crie o ambiente virtual:**
```bash
git clone <url-do-repositorio>
cd "PyTutor AI"
python -m venv .venv
source .venv/bin/activate
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# edite o .env e adicione sua chave da OpenAI
```

**4. Suba o backend:**
```bash
uvicorn back.main:app --reload
```

**5. Em outro terminal, suba o frontend:**
```bash
streamlit run front/app.py
```

Acesse `http://localhost:8501` no navegador.

## 🔑 Variáveis de Ambiente

```env
API_KEY=sk-proj-sua-chave-aqui
API_URL=http://127.0.0.1:8000
```

## 📚 Contexto Acadêmico

Atividade do **Módulo 3 — Avaliação de Modelos de Linguagem** da Pós-Graduação em IA para Devs.

O módulo aborda técnicas para medir e comparar a qualidade de respostas geradas por LLMs, explorando métricas automáticas como Perplexidade e BLEU como alternativas à avaliação humana.
