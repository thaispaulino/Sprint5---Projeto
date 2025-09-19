import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Explorador de CSV", layout="centered")
st.header("Explorador de CSV 📊")
st.write("Carregue um CSV e gere um histograma interativo com Plotly Express.")

arq = st.file_uploader("Selecione um arquivo CSV", type=["csv"])
df = None
if arq is not None:
    try:
        df = pd.read_csv(arq)
    except UnicodeDecodeError:
        arq.seek(0)
        df = pd.read_csv(arq, encoding="latin-1", sep=";")

if df is not None:
    st.write("Prévia dos dados:")
    st.write(df.head())

    cols_num = df.select_dtypes(include="number").columns
    if len(cols_num) == 0:
        st.warning("Nenhuma coluna numérica encontrada.")
    else:
        col = st.selectbox("Coluna para o histograma:", cols_num)
        nbins = st.slider("Número de bins", 5, 100, 30)
        if st.button("Gerar histograma"):
            fig = px.histogram(df, x=col, nbins=nbins, title=f"Histograma de {col}")
            st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Envie um CSV para começar.")
