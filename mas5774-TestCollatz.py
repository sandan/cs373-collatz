#!/usr/bin/env python3

# -------------------------------
# Copyright (C) 2014
# Mark Sandan
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        r    = StringIO("10 1\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  10)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        r    = StringIO("")
        j = collatz_read(r)
        self.assertListEqual([], j)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(900, 1000)
        self.assertNotEqual(v, 0)

    def test_eval_6 (self) :
        v = collatz_eval(100, 100)
        self.assertNotEqual(v, 0)

    def test_eval_7 (self) :
        try:
            collatz_eval(0,1)
        except AssertionError:
            pass
        except e:
            self.fail('Unexpected exception raised: ',e)
        else:
            self.fail('AssertionError not raised')

    def test_eval_8 (self) :
        try:
            collatz_eval(1,0)
        except AssertionError:
            pass
        except e:
            self.fail('Unexpected exception raised: ',e)
        else:
            self.fail('AssertionError not raised')

    def test_eval_9 (self) :
        try:
            collatz_eval(0,0)
        except AssertionError:
            pass
        except e:
            self.fail('Unexpected exception raised: ',e)
        else:
            self.fail('AssertionError not raised')


    def test_eval_10 (self) :
        v = collatz_eval(20, 20)
        self.assertEqual(v, 8)
        w = collatz_eval(19, 19)
        self.assertEqual(w, 21)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")


    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    def test_solve_3 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

main()
