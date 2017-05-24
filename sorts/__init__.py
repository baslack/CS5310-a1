import random


random.seed(1249070643579)


def swap(a, i, j):
    """
    swaps two indexed elements
    from a given list
    :param a: the list
    :param i: index of first element
    :param j: index of second element
    :return: None
    """
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def findpivot_1(a, m, p):
    """
    returns an index of the first
    element in the array slice from
    m to p
    :param a: the list 
    :param m: first index
    :param p: last index
    :return: m
    """
    return m


def findpivot_m(a, m, p):
    """
    returns the index of the median
    value element of a given list with
    a starting index of m,  ending index
    if p and a middle index calculated 
    between them.
    :param a: the list
    :param m: start index
    :param p: end index
    :return: median value index
    """
    o = (m+p)//2
    values = list()
    values.append(a[m])
    values.append(a[o])
    values.append(a[p])
    values.sort()
    median_value = values[1]
    if a[m] == median_value:
        return m
    elif a[o] == median_value:
        return o
    else:
        return p


def findpivot_r(a, m, p):
    """
    generates a random index
    for a given list, between
    the starting index m and 
    the end index p.
    :param a: the list
    :param m: the starting index
    :param p: the end index
    :return: the randome index between m and p
    """
    return random.randint(m,p)


def partition(pivot, a, m, p):
    """
    partitions a give list into two
    disjoint slices around a given
    pivot value
    :param pivot: index of the pivot
    :param a: a list
    :param m: index of the starting element 
    :param p: index of the ending element
    :return: the index of the partition point
    """
    if not(m < p):
        return -1
    pivot_value = a[pivot]
    swap(a, pivot, m)
    i = m
    j = p + 1
    while i < j:
        while True:
            i += 1
            try:
                if (a[i] >= pivot_value):
                    break
            except IndexError:
                break
        while True:
            j -= 1
            try:
                if (a[j] <= pivot_value):
                    break
            except IndexError:
                break
        if i < j:
            swap(a, i, j)
    swap(a, m, j)
    return j


def quicksort(findpivot, a, m, p):
    """
    quicksorts a given list using
    a findpivot function supplied
    as the first paramenter. Said
    function returns an index of 
    the list and takes the form:
    int findpivot(a, m, p)
    :param findpivot: pivot function
    :param a: the list
    :param m: starting index
    :param p: ending index
    :return: None
    """
    if p <= m:
        return
    else:
        pivot = findpivot(a, m, p)
        into = partition(pivot, a, m, p)
        quicksort(findpivot, a, m, into - 1)
        quicksort(findpivot, a, into + 1, p)


def select(findpivot, a, m, p, k):
    """
    returns the value of the kth
    smallest element of a given list.
    Requires the ust of a findpivot 
    function of the following type
    int findpivot(a, m, p)
    :param findpivot: the pivot func
    :param a: the list
    :param m: the starting index
    :param p: the ending index
    :param k: the kth
    :return: the value of the kth element
    """
    if p == m and m == k - 1:
        return a[m]
    elif p < m:
        return None
    else:
        pivot = findpivot(a, m, p)
        into = partition(pivot, a, m, p)
        if into == k-1:
            return a[into]
        elif into > k-1:
            return select(findpivot, a, m, into - 1, k)
        else:
            return select(findpivot, a, into + 1, p, k)


def generate_nondecreasing_a(n, max):
    """
    generates a list of non-
    decreasing integers in the
    range of 1 to max
    :param n: number of ints
    :param max: max value of int
    :return: 
    """
    a = generate_random_a(n, max)
    a.sort()
    return a

def generate_nonincreasing_a(n, max):
    """
    generates a list of non-
    increasing integers in the
    range of 1 to max
    :param n: number of ints
    :param max: max value of int
    :return: 
    """
    a = generate_nondecreasing_a(n, max)
    a.reverse()
    return a

def generate_random_a(n, max):
    """
        generates a list of random 
        integers in the range of 1 
        to max.
        :param n: number of ints
        :param max: max value of int
        :return: 
        """
    a = list()
    for i in range(n):
        a.append(random.randint(1, max))
    return a