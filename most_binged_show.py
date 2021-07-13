import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
plt.rcParams['font.size'] = 10


def execute_pd():
    data = pd.read_csv(
        'ViewingActivity.csv',
        usecols=['Duration', 'Title', 'Video Type']
    )
    data['Duration'] = pd.to_timedelta(data['Duration'])

    all_television = data[['Duration', 'Title', 'Video Type']]
    all_television = all_television[all_television['Video Type'].str.match('Television')]

    show_details = data.Title.str.split(":", expand=True, n=2)
    all_television['show_name'] = show_details[0]
    all_television = all_television.drop(['Video Type', 'Title'], axis=1)

    all_television = all_television.groupby(['show_name']).sum().reset_index().sort_values(by=['Duration'], inplace=False, ascending=False)
    all_television['hours'] = all_television['Duration'] / np.timedelta64(1, 'h')

    sns.set_style('whitegrid')
    plt.figure(figsize=(20, 10))
    ax = sns.barplot(y="show_name",
                     x="hours",
                     data=all_television.head(10),
                     palette="twilight_r",
                     alpha=0.7,
                     orient="h")
    for p in ax.patches:
        ax.text(p.get_width() + 1,
                p.get_y() + p.get_height() / 2,
                '{:1.2f}'.format(p.get_width()),
                horizontalalignment='left',
                verticalalignment='center')
    plt.xlabel("Hours")
    plt.ylabel("Shows")
    plt.title("Most Watched Shows")
    plt.show(block=True)


if __name__ == '__main__':
    execute_pd()
