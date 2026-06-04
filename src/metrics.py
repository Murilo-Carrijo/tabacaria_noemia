def valor_parado(df):

    return (
        df.groupby("Produto")["Total_Preco_Custo"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
    )


def top_dez(df, coluna):

    return (
        df.groupby('Produto')[coluna]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def abaixo_minimo(df):

    return df[
        (df['Quantidade']) < int(df['estoque_minimo'])
    ]


def excesso_estoque(df):

    return df[
        (df['Quantidade']) < (int(df['estoque_minimo']) * 3)
    ]


def baixa_margem_alto_estoque(df):

    return df[
        (df["margem"] < 0.10)
        &
        (df["Quantidade"] > 50)
    ]


def vendas_por_mes(df):
    vendas = (
        df.groupby(df['data'].dt.to_period('M'))['total_vendas']
        .sum()
        .sort_index()
    )
    vendas.index = vendas.index.astype(str)
    return vendas


def vendas_por_dia(df):
    daily_sales = (
        df.groupby('datas')['total_venda']
        .sum()
        .sort_index(ascending=False)
    )

    order_by_value = daily_sales.sort_values(ascending=False)

    return {
        "ultimos_trinta_dias": daily_sales.head(30),
        "top_cinco": order_by_value.head(5)
    }


def top_produtos_quantidade(df):
    return (
        df.groupby('produto')['quantidade']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def top_produtos_lucro(df):
    return (
        df.groupby('produto')['total_lucro']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def top_prejuizos(df):
    return (
        df.groupby('produto')['total_lucro']
        .sum()
        .sort_values(ascending=True)
        .head(10)
    )


def correlation_matrix(df):
    return df[
        ['total_venda', 'total_custo', 'total_lucro', 'quantidade']
        ].corr()
