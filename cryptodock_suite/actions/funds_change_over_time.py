import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def funds_change_over_time(params, Sdk) :
    """
        [ {'cycles': 10, 'avg_funds': 0.15, 'current_funds': 0.15} ]
    """

    if params['test'] :
        data = test_data()
    else :
        data = Sdk.Local.get_events(
            type="fill",
            strategy=params['strategy'],
            session=params['session'],
            fields=['avg_funds', 'current_funds', 'cycles']
        )

    df = pd.DataFrame({
        'Average Funds': [el['avg_funds'] for el in data],
        'Current Funds': [el['current_funds'] for el in data],
    }, index=[el['cycles'] for el in data])

    df['Current Funds'].plot(color="blue", linewidth=1, marker='o', markersize=4, markeredgecolor='black', markeredgewidth=1, markerfacecolor='blue', y="Current Funds", alpha=0.3)
    df['Average Funds'].plot(color="red", linewidth=2, marker='o', markersize=6, markeredgecolor='black', markeredgewidth=1, markerfacecolor='red', y="Average Funds", alpha=0.6)

    plt.title('Current Funds and Cumulative Avgerage Funds')
    plt.xlabel('Cycles Across Time')
    plt.ylabel('Funds')
    plt.show()

def test_data() :
    return []
