import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def order_type_ratio(params, Sdk) :
    """
        Expected data: [ {'margin': 8, 'limit': 10, 'market': 20} ]
    """

    if params['test'] :
        data = test_data()
    else :
        data = self.Sdk.Local.get_events(
            type="order",
            strategy=self.params['strategy'],
            session=self.params['session'],
            fields=['margin', 'limit', 'market']
        )

    margin_avg = len(data) / data[-1]['margin']
    limit_avg = len(data) / data[-1]['limit']
    market_avg = len(data) / data[-1]['market']

    df = pd.DataFrame({
        'ratio': [margin_avg, limit_avg, market_avg]
    }, index=['Market', 'Limit', 'Margin'])

    df.plot.pie(y="ratio")
    plt.title('Ratio Between "Market", "Margin", and "Limit" Orders')
    plt.show()

def test_data() :
    return [
        {'margin': 0, 'limit': 0, 'market': 0},
        {'margin': 0, 'limit': 0, 'market': 1},
        {'margin': 0, 'limit': 0, 'market': 2},
        {'margin': 0, 'limit': 0, 'market': 3},
        {'margin': 0, 'limit': 1, 'market': 3},
        {'margin': 1, 'limit': 1, 'market': 3},
        {'margin': 1, 'limit': 2, 'market': 3},
        {'margin': 1, 'limit': 3, 'market': 3},
        {'margin': 1, 'limit': 4, 'market': 3},
        {'margin': 1, 'limit': 5, 'market': 3},
        {'margin': 1, 'limit': 5, 'market': 4},
        {'margin': 2, 'limit': 5, 'market': 4},
        {'margin': 3, 'limit': 5, 'market': 4},
        {'margin': 3, 'limit': 6, 'market': 4},
    ]
