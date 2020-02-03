import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def cancel_rate_over_time(params, Sdk) :
    """
        [ {'cancel_count': 10} ]
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
        data = [{'cancel_count': n} for n in range(random.randint(50,1000)) for l in range(0, random.randint(1,100))]
    else :
        data = Sdk.Local.get_events(
            strategy=params['strategy'],
            session=params['session'],
            fields=['cancel_count']
        )

    list = [el['cancel_count'] for el in data]
    group_len = int(math.ceil(len(list)) / WINDOW)
    matrix = [list[i:i + WINDOW] for i in range(0, len(list), WINDOW)]
    rate_list = [len(np.unique(el)) for el in matrix]
    rate_of_change = pd.DataFrame(rate_list, index=[i * WINDOW for i in range(0, len(rate_list))], columns=["Cancels"])
    rate_of_change.plot(color="r", linewidth=0.5, marker='o', markersize=3, markeredgecolor='black', markeredgewidth=0.5, markerfacecolor='red', y="Cancels", alpha=0.5)
    plt.title('Cancel Rate OT ({}c)'.format(WINDOW))
    plt.xlabel('Periods')
    plt.ylabel('Cancels During Period')
    plt.xticks([int(i * WINDOW) for i in range(0, len(rate_list))])
    plt.show()
