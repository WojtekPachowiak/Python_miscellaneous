import multiprocessing
import time

    
start = time.perf_counter()

def do_smth(sec):
    print(f"Sleeping {sec} second(s)")
    time.sleep(sec)
    print("Done sleeping...\n")

threads = []
if __name__ == '__main__':

    for _ in range(100):
        t = multiprocessing.Process(target=do_smth, args=[5.])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()

    print(f"Finished in {finish - start}(s)")