import pandas as pd


def preprocess(df):
    df['data'] = pd.to_datetime(df['datas'])
    df['total_vendas'] = df['valor_venda'] * df['quantidade']
    df['total_custo'] = df['valor_custo'] * df['quantidade']
    df['total_lucro'] = df['valor_venda'] - df['total_custo']
    return df


def agrupar_produtos_com_menos_nome(df, limite=10):
    contagem_produtos = df['produto'].value_counts()
    produtos_para_agrupar = contagem_produtos[contagem_produtos < limite].index
    df['produto'] = df['produto'].apply(
        lambda x: 'Outros' if x in produtos_para_agrupar else x
    )
    return df
