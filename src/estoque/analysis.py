def top_dez(df, coluna):
    return (
        df.groupby('Produto')[coluna]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
