# #!/usr/bin/env python

from sorts import *
import time
import sys
import re
from copy import *

def average_qsort_time(findpivot, n, max, iter, bAvg):
    """
    returns the average sort time for a given
    list of length n. The bAvg parameter determines
    whether the average or the worst case of input
    will be generated.
    :param findpivot: function  of form <int> <funcname> (a, m, p)
    :param n: <int> length of the list to be generated
    :param max: <int> maximum value of elements of the list
    :param iter: <int> number of iterations to average
    :param bAvg: <bool> whether or not to generate the average case (true) or worst case(false)
    :return: <int> the index of the list to be the pivot
    """
    if bAvg:
        _a = generate_random_a(n, max)
    else:
        _a = generate_nondecreasing_a(n, max)
    total_time = 0;
    a = deepcopy(_a)
    if n == 10:
        print "qsort{0}, n = 10, starting list".format(repr(findpivot))
        print "{0}".format(a)
    for i in range(iter):
        a = deepcopy(_a)
        start_time = time.clock()
        quicksort(findpivot, a, 0, n-1)
        end_time = time.clock()
        total_time += (end_time-start_time)
    if n == 10:
        print "qsort{0}, n = 10, ending list".format(repr(findpivot))
        print "{0}".format(a)
    average_time = total_time / iter
    return average_time


def average_select_time(findpivot, n, max, iter, bAvg):
    """
        returns the average select time for a given
        list of length n. The bAvg parameter determines
        whether the average or the worst case of input
        will be generated.
        :param findpivot: function  of form <int> <funcname> (a, m, p)
        :param n: <int> length of the list to be generated
        :param max: <int> maximum value of elements of the list
        :param iter: <int> number of iterations to average
        :param bAvg: <bool> whether or not to generate the average case (true) or worst case(false)
        :return: <int> the index of the list to be the pivot
    """
    if not bAvg:
        k = n
        _a = generate_nondecreasing_a(n, max)
    else:
        k = random.randint(1, n)
        _a = generate_random_a(n, max)


    total_time = 0;

    a = deepcopy(_a)
    if n == 10:
        print "select{0}, n = 10, starting list, k: {1}".format(repr(findpivot), k)
        print "{0}".format(a)
    for i in range(iter):
        a = deepcopy(_a)
        start_time = time.clock()
        select(findpivot, a, 0, n-1, k)
        end_time = time.clock()
        total_time += (end_time-start_time)
    if n == 10:
        print "select{0}, n = 10, ending list, k: {1}".format(repr(findpivot), k)
        print "{0}".format(a)
    average_time = total_time / iter
    return average_time


if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    _n = list()
    _max = 0
    _iter = 0
    filename = "a1.csv"

    #print(sys.argv)
    #print(len(sys.argv))

    #parse the command line arguments
    i = 1
    while (i <= len(sys.argv)-1):
        #set the number to check
        #loop until you hit something
        #that is not a number
        if sys.argv[i] == "-n":
            while True:
                try:
                    i += 1
                    _n.append(int(sys.argv[i]))
                except Exception:
                    break
        #set max
        elif sys.argv[i] == "-m":
            try:
                i += 1
                _max = int(sys.argv[i])
                i += 1
            except TypeError:
                continue
        #set iterations
        elif sys.argv[i] == "-i":
            try:
                i += 1
                _iter = int(sys.argv[i])
                i += 1
            except TypeError:
                continue
        #set filename
        elif sys.argv[i] == "-f":
            try:
                i += 1
                filename = sys.argv[i]
                i += 1
            except Exception:
                print "-f Invalid Filename"
        else:
            i += 1
            print "a1 usage: -n <int> ... <int> -m <int> -i <int> -f <string>\n\r"
            exit(-1)


    if len(_n) == 0:
        _n = [10,  20, 40, 80, 160, 320, 640, 1280, 2560]
        #_n = [10, 20, 40, 80, 160, 320, 640]
        #_n = [10, 20, 40]


    if _max == 0:
        _max = 10000


    if _iter == 0:
        _iter = 1000

    print "n:{0}, max:{1}, iter:{2}, filename:{3}\n\r".format(_n, _max, _iter, filename)

    _findpivots = [findpivot_1, findpivot_r, findpivot_m]

    pattern = re.compile(".*(findpivot_.+?).*")

    with open(filename, "w") as f:
        f.truncate()
        for findpivot in _findpivots:
            findpivot_str = pattern.search(repr(findpivot)).group(1)
            for n in _n:
                avg = average_qsort_time(findpivot, n, _max, _iter, True)
                print(u"qsort:{0} avg, {1}, {2} \u03BCs".format(findpivot_str, n, avg*(10**6)))
                f.write("qsort:{0} avg, {1}, {2}\n\r".format(findpivot_str, n, avg*(10**6)))
            for n in _n:
                avg = average_qsort_time(findpivot, n, _max, _iter, False)
                print(u"qsort:{0} worst, {1}, {2} \u03BCs".format(findpivot_str, n, avg*(10**6)))
                f.write("qsort:{0} worst, {1}, {2}\n\r".format(findpivot_str, n, avg*(10**6)))
        _findpivots.remove(findpivot_m)
        for findpivot in _findpivots:
            findpivot_str = pattern.search(repr(findpivot)).group(1)
            for n in _n:
                avg = average_select_time(findpivot, n,  _max, _iter, True)
                print(u"select:{0} avg, {1}, {2} \u03BCs".format(findpivot_str, n, avg*(10**6)))
                f.write("select:{0} avg, {1}, {2}\n\r".format(findpivot_str, n, avg*(10**6)))
            for n in _n:
                avg = average_select_time(findpivot, n, _max, _iter, False)
                print(u"select:{0} worst, {1}, {2} \u03BCs".format(findpivot_str, n, avg*(10**6)))
                f.write("select:{0} worst, {1}, {2}\n\r".format(findpivot_str, n, avg*(10**6)))