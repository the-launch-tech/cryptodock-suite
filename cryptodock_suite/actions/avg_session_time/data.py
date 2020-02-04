import random
import requests
import datetime

def data() :
    response = requests.get("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")
    WORDS = response.content.splitlines()
    list = []
    session_count = random.randint(1, 20)
    start_time = datetime.datetime.now()

    for s in range(1, session_count) :
        end_time = start_time + datetime.timedelta(seconds=random.randint(1800, 1800**2))
        list.append({
            'start_time': start_time,
            'end_time': end_time,
            'session_label': random.choice(WORDS).decode("utf-8")
        })
        start_time = end_time
    return list
