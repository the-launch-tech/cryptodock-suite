import pandas as pd
import matplotlib.pyplot as plt
from .data import data


def side_ratio(params, Sdk) :
    """
        [ {'maker': 8, 'taker': 10} ]
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
        events = self.Sdk.Local.get_events(
            type="order",
            strategy=self.params['strategy'],
            session=self.params['session'],
            fields=['maker', 'taker']
        )

    maker_avg = len(events) / events[-1]['maker']
    taker_avg = len(events) / events[-1]['taker']

    df = pd.DataFrame({
        'ratio': [maker_avg, taker_avg]
    }, index=['Taker', 'Maker'])

    df.plot.pie(y="ratio")
    plt.title('Ratio Between "Maker" and "Taker" Orders')
    plt.show()
