import random

def data() :
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
