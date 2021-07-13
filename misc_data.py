import pandas as pd


def execute_pd():
    data = pd.read_csv(
        'ViewingActivity.csv',
        usecols=['Duration']
    )
    data['Duration'] = pd.to_timedelta(data['Duration'])

    print(data['Duration'].sum())
    print(f"Seconds: {data['Duration'].sum().total_seconds()}")
    print(f"Minutes: {data['Duration'].sum().total_seconds() / 60}")
    print(f"Hours: {data['Duration'].sum().total_seconds() / 60 / 60}")
    # LOTR extended edition has a runtime of 686 minutes


if __name__ == '__main__':
    execute_pd()
