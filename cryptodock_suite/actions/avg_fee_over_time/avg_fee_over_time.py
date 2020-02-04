import pandas as pd
import matplotlib.pyplot as plt
from .data import data

def avg_fee_over_time(params, Sdk) :
    """
        [ {'cycles': 10, 'avg_fee': 0.15, 'fee': 0.15} ]
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
            fields=['avg_fee', 'fee', 'cycles']
        )

    df = pd.DataFrame({
        'Average Fee': [el['avg_fee'] for el in events],
        'Fee': [el['fee'] for el in events],
    }, index=[el['cycles'] for el in events])

    df['Fee'].plot(color="blue", linewidth=0.4, marker='o', markersize=2, markeredgecolor='blue', markeredgewidth=0.4, markerfacecolor='blue', y="Fees", alpha=0.3)
    df['Average Fee'].plot(color="red", linewidth=0.8, marker='o', markersize=3, markeredgecolor='red', markeredgewidth=0.8, markerfacecolor='red', y="Average Fee", alpha=0.6)

    plt.title('Fee and Avg Cumulative Fee')
    plt.xlabel('Cycles Across Time')
    plt.ylabel('Fees')
    plt.show()
