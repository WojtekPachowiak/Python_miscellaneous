import concurrent.futures
import time
start = time.perf_counter()

def do_smth(sec):
    print(f"Sleeping {sec} second(s)")
    time.sleep(sec)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]

    #print as soon as thread completes
    # results = [executor.submit(do_smth, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    #wait until every thread completes
    results = executor.map(do_smth, secs)
    for result in results:
        print(result)


finish = time.perf_counter()

print(f"Finished in {finish - start}(s)")