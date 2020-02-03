import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def test_data() :
    list = []
    max_cycles = 5000
    max_fills = int(max_cycles / 100)
    max_size = 10000
    rate = 0.03
    fill_cycles = [random.randint(1, max_cycles) for r in range(1, max_fills)]
    for n in range(1, max_cycles) :
        if n in fill_cycles :
            list.append({
                'cycles': n,
                'fee': rate * random.randint(1, max_size),
                'avg_fee': sum([l['fee'] for l in list]) / len(list) if len(list) > 0 else rate
            })
    return list

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
        data = test_data()
    else :
        data = Sdk.Local.get_events(
            type="fill",
            strategy=params['strategy'],
            session=params['session'],
            fields=['avg_fee', 'fee', 'cycles']
        )

    df = pd.DataFrame({
        'Average Fee': [el['avg_fee'] for el in data],
        'Fee': [el['fee'] for el in data],
    }, index=[el['cycles'] for el in data])

    df['Fee'].plot(color="blue", linewidth=0.4, marker='o', markersize=2, markeredgecolor='blue', markeredgewidth=0.4, markerfacecolor='blue', y="Fees", alpha=0.3)
    df['Average Fee'].plot(color="red", linewidth=0.8, marker='o', markersize=3, markeredgecolor='red', markeredgewidth=0.8, markerfacecolor='red', y="Average Fee", alpha=0.6)

    plt.title('Fee and Avg Cumulative Fee')
    plt.xlabel('Cycles Across Time')
    plt.ylabel('Fees')
    plt.show()
