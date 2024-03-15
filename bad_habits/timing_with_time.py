import time


def timing_with_time() -> None:
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(end, -start)


def proper_timing_with_time() -> None:
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end, -start)
