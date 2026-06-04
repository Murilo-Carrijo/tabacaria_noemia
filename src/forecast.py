from statsmodels.tsa.arima.model import ARIMA
import pandas as pd


def forecast_stock(serie):

    model = ARIMA(
        serie,
        order=(5, 1, 0)
    )

    fit = model.fit()

    return fit.forecast(30)


def previsao_proximo_mes(df_vendas):
    """
    Previsão simples baseada na média dos últimos 3 meses.
    """

    df = df_vendas.copy()

    df["datas"] = pd.to_datetime(df["datas"])

    vendas_mensais = (
        df.groupby([
            pd.Grouper(key="datas", freq="M"),
            "produto"
        ])["quantidade"]
        .sum()
        .reset_index()
    )

    previsoes = []

    for produto in vendas_mensais["produto"].unique():

        produto_df = (
            vendas_mensais[
                vendas_mensais["produto"] == produto
            ]
            .sort_values("datas")
        )

        ultimos_3 = produto_df.tail(3)

        media = ultimos_3["quantidade"].mean()

        previsoes.append({
            "produto": produto,
            "previsao_mes": round(media, 0)
        })

    return pd.DataFrame(previsoes)


def sugestao_compras(df_previsao, df_estoque):

    estoque = df_estoque.copy()

    estoque = estoque.rename(columns={
        "Produto": "produto",
        "Quantidade": "estoque_atual"
    })

    resultado = df_previsao.merge(
        estoque[
            [
                "produto",
                "estoque_atual",
                "estoque_minimo"
            ]
        ],
        on="produto",
        how="left"
    )
    resultado["estoque_minimo"] = pd.to_numeric(
        resultado["estoque_minimo"],
        errors="coerce"
    )

    resultado["quantidade_comprar"] = (
        resultado["previsao_mes"]
        + resultado["estoque_minimo"]
        - resultado["estoque_atual"]
    )

    resultado["quantidade_comprar"] = (
        resultado["quantidade_comprar"]
        .clip(lower=0)
    )

    return resultado.sort_values(
        "quantidade_comprar",
        ascending=False
    )
