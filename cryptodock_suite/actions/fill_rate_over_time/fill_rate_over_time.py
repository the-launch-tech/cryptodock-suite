import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from .data import data


def fill_rate_over_time(params, Sdk) :
    """
        [ {'fill_count': 10} ]
    """

    WINDOW = params['window'] if params['window'] else 1800
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
            strategy=params['strategy'],
            session=params['session'],
            fields=['fill_count']
        )

    list = [el['fill_count'] for el in events]
    group_len = int(math.ceil(len(list)) / WINDOW)
    matrix = [list[i:i + WINDOW] for i in range(0, len(list), WINDOW)]
    rate_list = [len(np.unique(el)) for el in matrix]
    rate_of_change = pd.DataFrame(rate_list, index=[i * WINDOW for i in range(0, len(rate_list))], columns=["Fills"])
    rate_of_change.plot(color="r", linewidth=0.5, marker='o', markersize=3, markeredgecolor='black', markeredgewidth=0.5, markerfacecolor='red', y="Fills", alpha=0.5)
    plt.title('Fill Rate OT ({}c)'.format(WINDOW))
    plt.xlabel('Periods')
    plt.ylabel('Fills During Period')
    plt.xticks([int(i * WINDOW) for i in range(0, len(rate_list))])
    plt.show()
