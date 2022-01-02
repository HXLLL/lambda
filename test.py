from lambda_calculus import *

# debug utils

import pdb
import unittest
import sys
sys.setrecursionlimit(100000000)

def to_int(x):
    return x(lambda x:x+1)(0)
def to_bool(x):
    return x(True)(False)
def to_pair(p, f_out = lambda x: x):
    return (f_out(First(p)), f_out(Second(p)))
def generate_val(n):
    return Zero if n == 0 else Succ(generate_val(n-1))

class TestLambda(unittest.TestCase):
    def verify_uninary(self, f, std, vals, f_in, f_out):
        for n in vals:
            self.assertEqual(f_out(f(f_in(n))), std(n))
    def verify_binary(self, f, std, vals, f_in, f_out):
        for n1 in vals:
            for n2 in vals:
                self.assertEqual(f_out(f(f_in(n1))(f_in(n2))), std(n1, n2))
    
    def pair_uninary(self, f, std, f_in = lambda x: x, f_out = lambda x: x):
        self.verify_uninary(f, std, [(x,y) for x in range(10) for y in range(10)],
                lambda p: Pair(f_in(p[0]))(f_in(p[1])), f_out)

    def bool_uninary(self, f, std):
        self.verify_uninary(f, std, [True, False], Boolean, to_bool)
    def bool_binary(self, f, std):
        self.verify_binary(f, std, [True, False], Boolean, to_bool)

    def cmp_uninary(self, f, std):
        self.verify_uninary(f, std, range(10), UInt, to_bool)
    def cmp_binary(self, f, std):
        self.verify_binary(f, std, range(10), UInt, to_bool)

    def arith_uninary(self, f, std, val = range(10)):
        self.verify_uninary(f, std, val, UInt, to_int)
    def arith_binary(self, f, std):
        self.verify_binary(f, std, range(10), UInt, to_int)

    def test_pair(self):
        self.pair_uninary(First, lambda p: p[0])
        self.pair_uninary(Second, lambda p: p[1])

    def test_bool(self):
        self.assertEqual(to_bool(T), True)
        self.assertEqual(to_bool(F), False)
        
        self.bool_uninary(Not, lambda x: not x)
        self.bool_binary(And, lambda x,y: x and y)
        self.bool_binary(Or, lambda x,y: x or y)

    def test_natural_number(self):
        self.assertEqual(to_int(Zero), 0)
        self.assertEqual(to_int(One), 1)
        self.assertEqual(to_int(Two), 2)

        self.arith_uninary(Succ, lambda x: x+1)
        self.pair_uninary(PairNPlus1N, lambda p: (p[0]+1,p[0]), f_in = UInt,
                f_out = lambda p: (to_int(First(p)), to_int(Second(p))))
        # print(to_pair(Two(PairNPlus1N)(Pair(Zero)(Zero)), f_out = to_int))
        self.arith_uninary(Prev, lambda x: x-1, val=range(1,11))

    def test_arithmetic(self):
        self.arith_binary(Add, lambda x,y: x+y)
        # self.arith_binary(Multiply, lambda x,y: x*y)
        print(to_int(Multiply(UInt(0))(UInt(0))))

    def test_cmp(self):
        self.cmp_uninary(IsZero, lambda x: x == 0)



if __name__ == "__main__":
    unittest.main()
