import matplotlib.pyplot as plt


def plot_vendas_mes(vendas, periodo="mes"):
    plt.figure(figsize=(20, 10))
    vendas.plot(kind='bar')
    plt.title(f"Vendas por {periodo.capitalize()}")
    plt.xlabel("Data")
    plt.ylabel("Faturamento")
    plt.savefig(f"outputs/graficos/vendas_{periodo}.png")
    plt.close()


def plot_top_produtos(vendas_por_produto, tipo="lucro"):
    plt.figure(figsize=(15, 7))
    vendas_por_produto.plot(kind='bar')
    plt.title(f"Top 10 Produtos por Vendas ({tipo})")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento")
    plt.xticks(rotation=45, ha='right')

    for index, value in enumerate(vendas_por_produto):
        plt.text(
            index,
            value,
            f'{value:.2f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(f"outputs/graficos/top_produtos_{tipo}.png")
    plt.close()
