import seaborn as sns
import matplotlib.pyplot as plt


def plot_distributions(df):
    """
    plots all features
    :param df:
    :return:
    """
    plt.close('all')
    for column in df.columns:
        sns.distplot(df[column])
        plt.show()
    return None
