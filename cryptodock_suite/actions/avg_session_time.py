import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def avg_session_time(params, Sdk) :

    if params['test'] :
        data = test_data()
    else :
        data = Sdk.Local.get_events()

def test_data() :
    return []
