import streamlit as st
import plotly.express as px

from src.database import load_data
from src.preprocessing import enrich_stock_data
from src.metrics import top_dez
from src.visualization import (
  plot_data_column_h,
  plot_data_column_v
)
from src.config import TABLE_ESTOQUE

df = load_data(TABLE_ESTOQUE)
df = enrich_stock_data(df)

st.title("📦 Gestão de Estoque")

top = top_dez(df, 'Total_Preco_Custo')

fig = plot_data_column_h(
  top,
  "Valor em Estoque (R$)",
  "Produto",
  "Top 10 Produtos por Valor em Estoque"
  )

st.plotly_chart(fig, use_container_width=True)

produtos_quantidade = top_dez(df, 'Quantidade')

fig = plot_data_column_v(
  produtos_quantidade,
  "Quantidade",
  "Produto",
  "Top Produtos por Quantidade em Estoque"
  )

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Produtos por Estoque Mínimo")

estoque_minimo = top_dez(df, 'estoque_minimo')

fig = px.bar(
    x=estoque_minimo.values,
    y=estoque_minimo.index,
    orientation="h"
)

st.plotly_chart(fig, use_container_width=True)

baixo_estoque = df[
        df['Quantidade'] < df['estoque_minimo']
    ]

st.subheader("Produtos abaixo do estoque mínimo")

st.dataframe(baixo_estoque)
