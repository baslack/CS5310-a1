from sorts import *
import time
from copy import *

def average_qsort_time(findpivot, n, max, iter, bAvg):
    if bAvg:
        _a = generate_random_a(n, max)
    else:
        _a = generate_nondecreasing_a(n, max)
    total_time = 0;
    a = deepcopy(_a)
    if n == 10:
        print a
    for i in range(iter):
        a = deepcopy(_a)
        start_time = time.clock()
        quicksort(findpivot, a, 0, n-1)
        end_time = time.clock()
        total_time += (end_time-start_time)
    if n == 10:
        print(a)
    average_time = total_time / iter
    return average_time


def average_select_time(findpivot, n, max, iter, bAvg):
    if not bAvg:
        k = n
    else:
        k = random.randint(1, n)

    _a = generate_random_a(n, max)

    total_time = 0;

    a = deepcopy(_a)
    if n == 10:
        print(a)
    for i in range(iter):
        a = deepcopy(_a)
        start_time = time.clock()
        select(findpivot, a, 0, n-1, k)
        end_time = time.clock()
        total_time += (end_time-start_time)
    if n == 10:
        print(a)
    average_time = total_time / iter
    return average_time


if __name__ == "__main__":
    _findpivots = [findpivot_1, findpivot_r, findpivot_m]
    #_n = [10,  20, 40, 80, 160, 320, 640, 1280, 2560]
    _n = [10, 20, 40, 80, 160, 320, 640]
    #_n = [10, 20, 40]
    _max = 10000
    _iter = 1000
    with open("a1.csv", "w") as f:
        f.truncate()
        for findpivot in _findpivots:
            for n in _n:
                avg = average_qsort_time(findpivot, n, _max, _iter, True)
                f.write("qsort{0} avg, {1}, {2}\n\r".format(repr(findpivot), n, avg*10**6))
            for n in _n:
                avg = average_qsort_time(findpivot, n, _max, _iter, False)
                f.write("qsort{0} worst, {1}, {2}\n\r".format(repr(findpivot), n, avg*10**6))
        _findpivots.remove(findpivot_m)
        for findpivot in _findpivots:
            for n in _n:
                avg = average_select_time(findpivot, n,  _max, _iter, True)
                f.write("select{0} avg, {1}, {2}\n\r".format(repr(findpivot), n, avg*10**6))
            for n in _n:
                avg = average_qsort_time(findpivot, n, _max, _iter, False)
                f.write("select{0} worst, {1}, {2}\n\r".format(repr(findpivot), n, avg*10**6))