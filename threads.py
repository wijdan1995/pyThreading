import requests
import time
import concurrent.futures
import threading

t1 = time.perf_counter()
url = 'https://xa.sa/i7ChjE6'

def callURL():
    urlReq = requests.get(url)
    # print(urlReq.content)
    return (f'{urlReq}')

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(callURL) for _ in range(20)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')