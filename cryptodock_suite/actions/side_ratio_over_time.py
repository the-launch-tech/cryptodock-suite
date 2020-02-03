import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def side_ratio_over_time(params, Sdk) :

    if params['test'] :
        data = test_data()
    else :
        data = Sdk.Local.get_events()

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
