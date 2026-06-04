import streamlit as st
import plotly.express as px

from src.database import load_data
from src.preprocessing import enrich_seles_data
from src.forecast import (
    previsao_proximo_mes,
    sugestao_compras
)

df_vendas = load_data("TAB_VENDAS")
df_estoque = load_data("TAB_CAD_PRODUTO_ESTOQUE")

df_vendas = enrich_seles_data(df_vendas)

previsao = previsao_proximo_mes(df_vendas)

compras = sugestao_compras(
    previsao,
    df_estoque
)

st.title("📈 Previsão de Compras")

st.dataframe(
    compras,
    width="stretch"
)

top = compras.head(20)

fig = px.bar(
    top,
    x="produto",
    y="quantidade_comprar",
    title="Produtos com Maior Necessidade de Compra"
)

st.plotly_chart(
    fig,
    width="stretch"
)
