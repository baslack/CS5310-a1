import random

random.seed(1249070643579)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def findpivot_1(a, m, p):
    return m


def findpivot_m(a, m, p):
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
    return random.randint(m,p)


def partition(pivot, a, m, p):
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
    if p <= m:
        return
    else:
        pivot = findpivot(a, m, p)
        into = partition(pivot, a, m, p)
        quicksort(findpivot, a, m, into - 1)
        quicksort(findpivot, a, into + 1, p)


def generate_nondecreasing_a(n, max):
    a = generate_random_a(n, max)
    a.sort()
    return a

def generate_nonincreasing_a(n, max):
    a = generate_nondecreasing_a(n, max)
    a.reverse()
    return a

def generate_random_a(n, max):
    a = list()
    for i in range(n):
        a.append(random.randint(1, max))
    return a