import pandas as pd


def preprocess(df):
    df = df.drop(columns=['id_estoque', 'data_vencimento'])
    cols_num = [
        'Preco_Custo',
        'Preco_Venda',
        'Quantidade',
        'Total_Preco_Custo',
        'Total_Preco_Venda',
        'estoque_minimo',
    ]
    for col in cols_num:
        if col in df.columns:
            s = df[col]
            if s.dtype == 'object':
                s = (
                    s.astype(str).str.strip()
                    .str.replace('.', '', regex=False)
                    .str.replace(',', '.', regex=False)
                )
            df[col] = pd.to_numeric(s, errors='coerce')

    # 2) agrega duplicados (1 linha por produto)
    dup_mask = df.duplicated(subset=['Produto'], keep=False)

    if dup_mask.any():
        dup = df.loc[dup_mask].copy()
        keep = df.loc[~dup_mask].copy()

        # Cod_ID: pega o menor (lexicográfico) => "068000" no exemplo
        # Se quiser "o primeiro não vazio", troque pelo .agg com lambda.
        aggregated = (
            dup.groupby('Produto', as_index=False)
               .agg({
                   'Cod_ID': 'min',
                   'Preco_Custo': 'mean',
                   'Preco_Venda': 'mean',
                   'Quantidade': 'sum',
                   'Total_Preco_Custo': 'sum',
                   'Total_Preco_Venda': 'sum',
                   'estoque_minimo': 'max',
               })
        )

        # 3) remove origem e adiciona linha agregada
        df = pd.concat([keep, aggregated], ignore_index=True)

    return df
