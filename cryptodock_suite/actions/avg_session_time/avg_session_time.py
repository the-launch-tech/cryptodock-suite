import pandas as pd
import matplotlib.pyplot as plt
from .data import data

def avg_session_time(params, Sdk) :
    """
        [ {'start_time': 10, 'end_time': 20, 'session_label': 'Test'} ]
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
            type="end",
            strategy=params['strategy'],
            fields=['start_time','end_time','session_label']
        )

    avg_hours = sum([(d['end_time'] - d['start_time']).total_seconds() * 3600 for d in events]) / len(events)
    list = [{'hours': (d['end_time'] - d['start_time']).total_seconds() * 3600, 'avg_hours': avg_hours, 'label': d['session_label']} for d in events]

    df = pd.DataFrame({
        'Hours': [el['hours'] for el in list],
        'Average Hours': [el['avg_hours'] for el in list],
    }, index=[el['label'] for el in list], columns=['Hours', 'Average Hours'])

    df['Hours'].plot(color="blue", linewidth=0.4, marker='o', markersize=2, markeredgecolor='blue', markeredgewidth=0.4, markerfacecolor='blue', y="Hours", alpha=0.6)
    df['Average Hours'].plot(color="red", linewidth=0.8, y="Average Hours", alpha=0.3)

    plt.title('Hours and Avg Hours session duration')
    plt.xlabel('Session Label')
    plt.ylabel('Hours')
    plt.show()
