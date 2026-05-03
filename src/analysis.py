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


def vendas_por_mes(df):
    vendas = (
        df.groupby(df['data'].dt.to_period('M'))['total_venda']
        .sum()
        .sort_index()
    )
    return vendas


def vendas_por_dia(df):
    daily_sales = (
        df.groupby('datas')['total_venda']
        .sum()
        .sort_index(ascending=False)
    )

    return {
        "ultimos_trinta_dias": daily_sales.head(30),
        "top_cinco": daily_sales.sort_values(ascending=False).head(5)
    }


def ticket_medio(df):
    clients = df.groupby('cliente').agg({
      'total_venda': 'sum',
      'quantidade': 'sum',
      'id_venda': 'count'
    })

    clients['ticket_medio'] = clients['total_venda'] / clients['id_venda']

    top_ticket_medio = clients.sort_values(
        by='ticket_medio', ascending=False
        ).head(10)

    print("\nTop ticket médio:")
    print(top_ticket_medio)

    output_xlsx = 'outputs/relatorios/top_ticket_medio.xlsx'
    top_ticket_medio.to_excel(output_xlsx, index=True)
    print(f"\nPlanilha salva em: {output_xlsx}")


def top_prejuizos(df):
    return (
        df.groupby('produto')['total_lucro']
        .sum()
        .sort_values(ascending=True)
        .head(10)
    )


def por_categoria(df):
    category_summary = df.groupby('categoria').agg({
      'total_venda': 'sum',
      'total_lucro': 'sum',
      'quantidade': 'sum'
    }).sort_values(by='total_venda', ascending=False)

    print("\nResumo por categoria:")
    print(category_summary)

    output_xlsx = 'outputs/relatorios/por_categoria.xlsx'
    category_summary.to_excel(output_xlsx, index=True)
    print(f"\nPlanilha salva em: {output_xlsx}")


def correlation_matrix(df):
    correlation = df[
        ['total_venda', 'total_custo', 'total_lucro', 'quantidade']
        ].corr()

    print("\nMatriz de correlação:")
    print(correlation)

    output_xlsx = 'outputs/relatorios/correlation_matrix.xlsx'
    correlation.to_excel(output_xlsx, index=True)
    print(f"\nPlanilha salva em: {output_xlsx}")


def analises(df):
    resume_do_lucro_por_produto = (
        df.groupby('produto')['total_lucro']
        .sum()
        .sort_values(ascending=False)
    )

    print("\nProdutos com o nome 'Paulistinha Tradicional':")
    print(resume_do_lucro_por_produto)

    output_xlsx = 'outputs/relatorios/resume_do_lucro_por_produto.xlsx'
    resume_do_lucro_por_produto.to_excel(output_xlsx, index=True)
    print(f"\nPlanilha salva em: {output_xlsx}")
