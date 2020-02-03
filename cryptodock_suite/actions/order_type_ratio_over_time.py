import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def order_type_ratio_over_time(params, Sdk) :

    if params['test'] :
        data = test_data()
    else :
        data = Sdk.Local.get_events()

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
