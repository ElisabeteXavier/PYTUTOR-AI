import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
st.set_page_config(page_title="PyTutor AI", layout="centered")

st.title("🤖 PyTutor AI")
st.write("Compare respostas de IA com métricas")

pergunta = st.text_area("Digite sua pergunta:")

if st.button("Perguntar"):
    if pergunta:

        with st.spinner("Pensando..."):

            res = requests.post(
                f"{API_URL}/chat/ask",
                json={"pergunta": pergunta})

            data = res.json()

            # 🔹 Respostas lado a lado
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📘 Resposta A (Teórica)")
                st.write(data["resposta_A"])
              
            with col2:
                st.subheader("🧪 Resposta B (Prática)")
                st.write(data["resposta_B"])



        st.subheader("📊 Métricas de Comparação")
        st.subheader("RESPOSTA A")
        st.write(f"Perplexidade: {data['metricas']['perplexidade_B']:.2f}")
        st.write(f"BLEU: {data['metricas']['bleu_B']:.2f}")
        st.subheader("RESPOSTA B")
        st.write(f"Perplexidade: {data['metricas']['perplexidade_A']:.2f}")
        st.write(f"BLEU: {data['metricas']['bleu_A']:.2f}")
