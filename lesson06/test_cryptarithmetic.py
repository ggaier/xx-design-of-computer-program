# coding=utf-8
from __future__ import division
from cryptarithmetic import solve
import time
from zebra_puzzle import timedcall #为了使用timed_calls 工具方法

examples = """TWO+TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()


def test():
    t0 = time.clock()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec: %s ' % timedcall(solve, example)
    print '%6.4f tot. ' % (time.clock() - t0)

test()
