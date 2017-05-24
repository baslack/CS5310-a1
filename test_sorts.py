#!/usr/bin/env python

from sorts import *
from copy import *

import unittest

_a = [5, 19, 7]

_b = [9, 120, 192, 154, 921, 12, 378, 123]

class test_sorts(unittest.TestCase):
    def test_findpivot_1(self):
        a = deepcopy(_a)
        self.assertEqual(findpivot_1(a,1,10), 1)


    def test_findpivot_m(self):
        a = deepcopy(_a)
        self.assertEqual(a[findpivot_m(a, 0, 2)], 7)


    def test_findpivot_r(self):
        a = deepcopy(_a)
        random.seed(7777)
        self.assertEqual(findpivot_r(a, 0, 2), 2)


    def test_generate_nondescreasing_a(self):
        a = generate_nondecreasing_a(10, 100)
        for i in range(9):
            self.assertTrue(a[i] <= a[i+1])


    def test_generate_nonincreasing_a(self):
        a = generate_nonincreasing_a(10, 100)
        for i in range(9):
            self.assertTrue(a[i] >= a[i+1])


    def test_generate_random_a(self):
        a = generate_random_a(10, 100)
        for item in a:
            self.assertTrue(item in range(1, 101))
        self.assertEqual(len(a), 10)


    def test_partition(self):
        a = deepcopy(_b)
        into = partition(7, a, 0, 7)
        self.assertEqual(into, 3)


    def test_quicksort1(self):
        a = deepcopy(_b)
        a0 = deepcopy(_b)
        quicksort(findpivot_1, a, 0, 7)
        a0.sort()
        self.assertEqual(a, a0)


    def test_quiicksortm(self):
        a = deepcopy(_b)
        a0 = deepcopy(_b)
        quicksort(findpivot_m, a, 0, 7)
        a0.sort()
        self.assertEqual(a, a0)

    def test_quiicksortr(self):
        a = deepcopy(_b)
        a0 = deepcopy(_b)
        quicksort(findpivot_r, a, 0, 7)
        a0.sort()
        self.assertEqual(a, a0)


    def test_select1(self):
        a = deepcopy(_b)
        _4th = select(findpivot_1, a, 0, 7, 4)
        self.assertEqual(_4th, 123)


    def test_selectr(self):
        a = deepcopy(_b)
        _4th = select(findpivot_r, a, 0, 7, 4)
        self.assertEqual(_4th, 123)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(test_sorts)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()