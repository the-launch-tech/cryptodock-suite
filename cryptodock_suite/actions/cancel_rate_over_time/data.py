import random

def data() :
    return [{'cancel_count': n} for n in range(random.randint(50,1000)) for l in range(0, random.randint(1,100))]
