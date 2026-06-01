import src.estoque.data_loader as data_loader
import src.estoque.preprocessing as preprocessing
import src.estoque.analysis as analysis
import src.estoque.visualization as visualization
import os


def estoque():
    df = data_loader.load_data()
    df = preprocessing.preprocess(df)

    os.makedirs('outputs/graficos/estoque', exist_ok=True)
    os.makedirs('outputs/relatorios/estoque', exist_ok=True)

    produtos_quantidade = analysis.top_dez(df, 'Quantidade')
    print(produtos_quantidade)
    visualization.plot_data_into_bar(
        produtos_quantidade,
        title="Top 10 Produtos por Quantidade em Estoque",
        xlabel="Produto",
        ylabel="Quantidade",
        filename="outputs/graficos/estoque/top_produtos_quantidade.png"
    )

    produtos_custo = analysis.top_dez(df, 'Total_Preco_Custo')
    print(produtos_custo)
    visualization.plot_data_into_bar(
        produtos_custo,
        title="Top 10 Produtos por Custo em Estoque",
        xlabel="Produto",
        ylabel="Custo",
        filename="outputs/graficos/estoque/top_produtos_custo.png"
    )

    estoque_minimo = analysis.top_dez(df, 'estoque_minimo')
    print(estoque_minimo)
    visualization.plot_data_into_bar(
        estoque_minimo,
        title="Top 10 Produtos por Estoque Mínimo",
        xlabel="Produto",
        ylabel="Estoque Mínimo",
        filename="outputs/graficos/estoque/top_produtos_estoque_minimo.png"
    )

    baixo_estoque = df[
        df['Quantidade'] < df['estoque_minimo']
    ]

    print(baixo_estoque[
        ['Produto', 'Quantidade', 'estoque_minimo']
    ])
