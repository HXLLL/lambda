import natural_number as N
from utils import *

P1 = First
P2 = Second

# Integer represented as (n1,n2) has value (n1-n2)
Zero = Pair(N.Zero)(N.Zero)
Succ = lambda p: Pair(N.Succ(P1(p)))(P2(p))
Prev = lambda p: Pair(P1(p))(N.Succ(P2(p)))

# arithmetic
Neg = lambda p: Pair(P2(p))(P1(p))
# (x1,y1) + (x2,y2) = (x1+y1,x2+y2)
Add = lambda x: lambda y: Pair(N.Add(P1(x))(P1(y)))(N.Add(P2(x))(P2(y)))
Minus = lambda x: lambda y: Add(x)(Neg(y))
# (x1,y1) * (x2,y2) = (x1*x2 + y1*y2, x1*y2 + y1*x2)
Multiply = lambda x: lambda y: \
  Pair(N.Add(N.Multiply(P1(x))(P1(y)))(N.Multiply(P2(x))(P2(y)))) \
  (N.Add(N.Multiply(P1(x))(P2(y)))(N.Multiply(P1(y))(P2(x))))

# cmp
IsZero = lambda x: N.Equal(P1(x))(P2(x))
IsPositive = lambda x: N.Greater(P1(x))(P2(x))
IsNegative = lambda x: N.Less(P1(x))(P2(x))
Equal = lambda x: lambda y: N.Equal(N.Add(P1(x))(P2(y)))(N.Add(P1(y))(P2(x)))
NotEqual = lambda x: lambda y: Not(Equal(x)(y))
Greater = lambda x: lambda y: IsPositive(Minus(x)(y))
Less = lambda x: lambda y: IsNegative(Minus(x)(y))
GreaterEqual = lambda x: lambda y: Not(Less(x)(y))
LessEqual = lambda x: lambda y: Not(Greater(x)(y))

# convert to int
N2Z = lambda x: Pair(x)(N.Zero)