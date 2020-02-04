import pandas as pd
import matplotlib.pyplot as plt
from .data import data


def order_type_ratio(params, Sdk) :
    """
        Expected events: [ {'margin': 8, 'limit': 10, 'market': 20} ]
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
            type="order",
            strategy=params['strategy'],
            session=params['session'],
            fields=['margin', 'limit', 'market']
        )

    margin_avg = len(events) / events[-1]['margin']
    limit_avg = len(events) / events[-1]['limit']
    market_avg = len(events) / events[-1]['market']

    df = pd.DataFrame({
        'ratio': [margin_avg, limit_avg, market_avg]
    }, index=['Market', 'Limit', 'Margin'])

    df.plot.pie(y="ratio")
    plt.title('Ratio Between "Market", "Margin", and "Limit" Orders')
    plt.show()
