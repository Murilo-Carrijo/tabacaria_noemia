from src.vendas.data_loader import load_data
from src.vendas.preprocessing import (
  preprocess,
  agrupar_produtos_com_menos_nome
)
from src.vendas.analysis import (
  top_produtos_quantidade,
  top_produtos_lucro,
  vendas_por_mes,
  vendas_por_dia,
  ticket_medio,
  top_prejuizos,
  por_categoria,
  correlation_matrix,
  analises
)
from src.vendas.visualization import plot_vendas_mes, plot_top_produtos
import os


def vendas():
    df = load_data()
    df = preprocess(df)
    df = agrupar_produtos_com_menos_nome(df, limite=10)

    os.makedirs('outputs/graficos', exist_ok=True)
    os.makedirs('outputs/relatorios', exist_ok=True)
    vendas_mes = vendas_por_mes(df)
    ultimos_trinta_dias, top_cinco = vendas_por_dia(df).values()
    produtos_lucro = top_produtos_lucro(df)
    produtos_quantidade = top_produtos_quantidade(df)
    produtos_prejuizo = top_prejuizos(df)

    plot_vendas_mes(vendas_mes, "mes")
    plot_vendas_mes(ultimos_trinta_dias, "dia")
    plot_vendas_mes(top_cinco, "top_cinco_dias")
    plot_top_produtos(produtos_lucro, "lucro")
    plot_top_produtos(produtos_quantidade, "quantidade")
    plot_top_produtos(produtos_prejuizo, "prejuizo")
    print("Análise concluída. Gráficos salvos em outputs/graficos/")

    ticket_medio(df)
    por_categoria(df)
    correlation_matrix(df)
    print("Análise concluída. Gráficos salvos em outputs/relatorios/")
    analises(df)
