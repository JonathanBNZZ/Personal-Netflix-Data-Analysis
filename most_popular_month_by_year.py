import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
plt.rcParams['font.size'] = 15


def execute_pd():
    data = pd.read_csv(
        'ViewingActivity.csv',
        usecols=['Start Time']
    )
    data['Start Time'] = pd.to_datetime(data['Start Time'], utc=True)
    data['year'] = data['Start Time'].dt.year
    data['month'] = data['Start Time'].dt.month_name()
    data['month'] = pd.Categorical(data['month'],
                                   categories=['January', 'February', "March", "April", "May",
                                               "June", "July", "August", "September", "October",
                                               "November", "December"],
                                   ordered=True)
    by_year = data.groupby('month')['year'].value_counts().reset_index(name="Frequency")

    sns.set_style('whitegrid')
    plt.figure(figsize=(15, 10))
    ax = sns.barplot(x=by_year['month'],
                     y=by_year['Frequency'],
                     hue=by_year['year'],
                     palette="magma_r",
                     alpha=0.7)
    for p in ax.patches:
        ax.text(x=p.get_x() + p.get_width() / 2,
                y=p.get_height() + 4,
                s='{:.0f}'.format(p.get_height()),
                horizontalalignment='center',
                verticalalignment='center')
    plt.ylabel("Number of Things Watched")
    plt.title("Most Watched Month By Year")

    plt.show(block=True)


if __name__ == '__main__':
    execute_pd()
