import streamlit as st

from src.database import load_data
from src.preprocessing import enrich_seles_data
from src.config import TABLE_VENDAS
from src.metrics import (
  vendas_por_mes,
  vendas_por_dia,
  top_produtos_lucro,
  top_produtos_quantidade,
  top_prejuizos,
  correlation_matrix
)
from src.visualization import plot_data_column_v

df = load_data(TABLE_VENDAS)
df = enrich_seles_data(df)

vendas_mes = vendas_por_mes(df)

st.title("💰 Gestão de Vendas")

fig = plot_data_column_v(
  vendas_mes,
  "Data",
  "Faturamento",
  "Vendas por Mês"
)

st.plotly_chart(fig, use_container_width=True)

ultimos_trinta_dias, top_cinco = vendas_por_dia(df).values()

fig = plot_data_column_v(
  ultimos_trinta_dias,
  "Data",
  "Faturamento",
  "Vendas por Dia"
)

st.plotly_chart(fig, use_container_width=True)

st.title("Dias com mais vendas na história")
st.dataframe(top_cinco)

produtos_lucro = top_produtos_lucro(df)
fig = plot_data_column_v(
  produtos_lucro,
  "Data",
  "Faturamento",
  "Top 10 Produtos mais lucrativos"
)

st.plotly_chart(fig, use_container_width=True)

produtos_quantidade = top_produtos_quantidade(df)
fig = plot_data_column_v(
  produtos_quantidade,
  "Data",
  "Faturamento",
  "Top 10 Produtos mais vendidos (qtd)"
)

st.plotly_chart(fig, use_container_width=True)

produtos_prejuizo = top_prejuizos(df)
fig = plot_data_column_v(
  produtos_prejuizo,
  "Data",
  "Faturamento",
  "Top 10 Produtos com maior prejuízo)"
)

st.plotly_chart(fig, use_container_width=True)

st.title("Matriz de correlação:")
st.dataframe(correlation_matrix(df))
