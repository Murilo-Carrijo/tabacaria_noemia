import plotly.express as px


def plot_data_column_h(fig, xlabel, ylabel, title):
    return px.bar(
        x=fig.values,
        y=fig.index,
        orientation="h",
        labels={
            "x": xlabel,
            "y": ylabel
        },
        title=title
    )


def plot_data_column_v(fig, xlabel, ylabel, title):
    return px.bar(
        x=fig.index,
        y=fig.values,
        orientation="v",
        labels={
            "x": xlabel,
            "y": ylabel
        },
        title=title
    )
