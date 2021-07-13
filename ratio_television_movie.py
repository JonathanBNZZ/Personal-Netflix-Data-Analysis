import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 15


def execute_pd():
    data = pd.read_csv(
        'ViewingActivity.csv',
        usecols=['Video Type']
    )

    # Total television and movie
    medium = data['Video Type'].value_counts()

    circle, pie = plt.subplots()

    pie.pie(
        x=medium,
        labels=medium.index,
        explode=[0.05] * 2,
        startangle=90,
        autopct=lambda x: '{:.0f}'.format(x*medium.sum()/100),
        colors=["#FF7C7C", "#88E1F2"],
        pctdistance=0.85
    )

    circle = plt.gcf()
    circle.gca().add_artist(plt.Circle((0, 0), 0.70, fc='White'))

    pie.axis('equal')
    plt.tight_layout()
    plt.title('Ratio of Movies to Television Show Episodes Watched on Netflix')

    plt.show(block=True)


if __name__ == '__main__':
    execute_pd()
