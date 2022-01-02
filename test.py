from utils import *
import natural_number as N
import integer as Z
from functools import partial

# debug utils

import pdb
import unittest
import sys
sys.setrecursionlimit(100000000)

# debug utils
def to_bool(x):
    return x(True)(False)
def N_to_int(x):
    return x(lambda x:x+1)(0)
def Z_to_int(x):
    return First(x)(lambda x: x+1)(0) - Second(x)(lambda x: x+1)(0)
def int_to_N(n):
    return N.UInt(n)
def int_to_Z(n):
    if (n<0): return Pair(N.Zero)(int_to_N(-n))
    else: return Pair(int_to_N(n))(N.Zero)
def to_pair(p, f_out = lambda x: x):
    return (f_out(First(p)), f_out(Second(p)))

class TestLambda(unittest.TestCase):
    def verify(self, f, std, n_args, vals, f_in, f_out):
        if (n_args == 1):
            for n in vals:
                self.assertEqual(f_out(f(f_in(n))), std(n))
        elif (n_args == 2):
            for n1 in vals:
                for n2 in vals:
                    self.assertEqual(f_out(f(f_in(n1))(f_in(n2))), std(n1, n2))
        else:
            assert(False)

    def pair_uninary(self, f, std, f_in = lambda x: x, f_out = lambda x: x):
        self.verify(f, std, 1, [(x,y) for x in range(10) for y in range(10)],
                lambda p: Pair(f_in(p[0]))(f_in(p[1])), f_out)

    def test_pair(self):
        self.pair_uninary(First, lambda p: p[0])
        self.pair_uninary(Second, lambda p: p[1])

    def test_bool(self):
        self.assertEqual(to_bool(T), True)
        self.assertEqual(to_bool(F), False)

        test_bool = partial(self.verify, vals=[True, False], f_in = Boolean, f_out = to_bool)
        
        test_bool(Not, lambda x: not x, 1)
        test_bool(And, lambda x,y: x and y, 2)
        test_bool(Or, lambda x,y: x or y, 2)

    def test_N_definition(self):
        self.assertEqual(N_to_int(N.Zero), 0)
        self.assertEqual(N_to_int(N.One), 1)
        self.assertEqual(N_to_int(N.Two), 2)

    def test_N_arithmetic(self):

        verify_arith = partial(self.verify, vals = range(10), f_in = N.UInt, f_out = N_to_int)

        verify_arith(N.Succ, lambda x: x+1, 1)
        self.verify(N.Prev, lambda x: x-1, 1, range(1,11), N.UInt, N_to_int)

        verify_arith(N.Add, lambda x,y: x+y, 2)
        verify_arith(N.Multiply, lambda x,y: x*y, 2)

    def test_N_cmp(self):
        verify_cmp = partial(self.verify, vals=range(10), f_in = N.UInt, f_out = to_bool)
        verify_cmp(N.IsZero, lambda x: x == 0, 1)
        verify_cmp(N.GreaterEqual, lambda x,y: x>=y, 2)
        verify_cmp(N.LessEqual, lambda x,y: x<=y, 2)
        verify_cmp(N.Equal, lambda x,y: x==y, 2)
        verify_cmp(N.NotEqual, lambda x,y: x!=y, 2)
        verify_cmp(N.Greater, lambda x,y: x>y, 2)
        verify_cmp(N.Less, lambda x,y: x<y, 2)
    
    def test_Z(self):
        R = range(-10, 10)

        self.assertEqual(Z_to_int(Z.Zero), 0)

        verify_arith = partial(self.verify, vals = R, f_in = int_to_Z, f_out = Z_to_int)

        verify_arith(Z.Succ, lambda n: n+1, 1)
        verify_arith(Z.Prev, lambda n: n-1, 1)
        verify_arith(Z.Neg, lambda n: -n, 1)
        verify_arith(Z.Add, lambda x,y: x+y, 2)
        verify_arith(Z.Minus, lambda x,y: x-y, 2)
        verify_arith(Z.Multiply, lambda x,y: x*y, 2)

        verify_cmp = partial(self.verify, vals=R, f_in=int_to_Z, f_out=to_bool)

        verify_cmp(Z.IsZero, lambda n: n==0, 1)
        verify_cmp(Z.IsPositive, lambda n: n>0, 1)
        verify_cmp(Z.IsNegative, lambda n: n<0, 1)

        verify_cmp(Z.Equal, lambda x,y: x==y, 2)
        verify_cmp(Z.NotEqual, lambda x,y: x!=y, 2)
        verify_cmp(Z.Greater, lambda x,y: x>y, 2)
        verify_cmp(Z.Less, lambda x,y: x<y, 2)
        verify_cmp(Z.GreaterEqual, lambda x,y: x>=y, 2)
        verify_cmp(Z.LessEqual, lambda x,y: x<=y, 2)
        

if __name__ == "__main__":
    unittest.main()
