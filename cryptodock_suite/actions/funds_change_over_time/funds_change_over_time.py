import pandas as pd
import matplotlib.pyplot as plt
from .data import data


def funds_change_over_time(params, Sdk) :
    """
        [ {'cycles': 10, 'avg_funds': 0.15, 'current_funds': 0.15} ]
    """

    SMALL_SIZE = 6
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
    plt.rc('font', size=SMALL_SIZE)
    plt.rc('axes', titlesize=MEDIUM_SIZE)
    plt.rc('axes', labelsize=MEDIUM_SIZE)
    plt.rc('xtick', labelsize=SMALL_SIZE)
    plt.rc('ytick', labelsize=SMALL_SIZE)
    plt.rc('legend', fontsize=MEDIUM_SIZE)
    plt.rc('figure', titlesize=BIGGER_SIZE)

    if params['test'] :
        events = data()
    else :
        events = Sdk.Local.get_events(
            type="fill",
            strategy=params['strategy'],
            session=params['session'],
            fields=['avg_funds', 'current_funds', 'cycles']
        )

    df = pd.DataFrame({
        'Average Funds': [el['avg_funds'] for el in events],
        'Current Funds': [el['current_funds'] for el in events],
    }, index=[el['cycles'] for el in events])

    df['Current Funds'].plot(color="blue", linewidth=1, marker='o', markersize=4, markeredgecolor='black', markeredgewidth=1, markerfacecolor='blue', y="Current Funds", alpha=0.3)
    df['Average Funds'].plot(color="red", linewidth=2, marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1, markerfacecolor='red', y="Average Funds", alpha=0.6)

    plt.title('Current Funds and Cumulative Avgerage Funds')
    plt.xlabel('Cycles Across Time')
    plt.ylabel('Funds')
    plt.show()
