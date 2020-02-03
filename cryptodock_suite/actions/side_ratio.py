import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def side_ratio(params, Sdk) :
    """
        [ {'maker': 8, 'taker': 10} ]
    """

    if params['test'] :
        data = test_data()
    else :
        data = self.Sdk.Local.get_events(
            type="order",
            strategy=self.params['strategy'],
            session=self.params['session'],
            fields=['maker', 'taker']
        )

    maker_avg = len(data) / data[-1]['maker']
    taker_avg = len(data) / data[-1]['taker']

    df = pd.DataFrame({
        'ratio': [maker_avg, taker_avg]
    }, index=['Taker', 'Maker'])

    df.plot.pie(y="ratio")
    plt.title('Ratio Between "Maker" and "Taker" Orders')
    plt.show()


def test_data() :
    return [
        {'maker': 0, 'taker': 0},
        {'maker': 1, 'taker': 0},
        {'maker': 2, 'taker': 0},
        {'maker': 2, 'taker': 1},
        {'maker': 3, 'taker': 1},
        {'maker': 3, 'taker': 2},
        {'maker': 3, 'taker': 2},
        {'maker': 4, 'taker': 2},
        {'maker': 5, 'taker': 3},
        {'maker': 5, 'taker': 4},
        {'maker': 5, 'taker': 5},
        {'maker': 5, 'taker': 6},
        {'maker': 5, 'taker': 7},
        {'maker': 5, 'taker': 8},
        {'maker': 6, 'taker': 8}
    ]
