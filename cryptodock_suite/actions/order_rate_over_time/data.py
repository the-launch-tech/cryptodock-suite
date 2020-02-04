import random

def data() :
    return [{'order_count': n} for n in range(random.randint(50,1000)) for l in range(0, random.randint(1,100))]
