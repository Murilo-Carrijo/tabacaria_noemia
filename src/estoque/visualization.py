import matplotlib.pyplot as plt


def plot_data_into_bar(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(20, 10))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for index, value in enumerate(data):
        plt.text(
            index,
            value,
            f'{value:.2f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
