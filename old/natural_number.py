from utils import *

# natural number
Zero = lambda x: lambda y: y # surprisingly, Zero = F
Succ = lambda x: lambda f: lambda y: f(x(f)(y))
One = Succ(Zero)
Two = Succ(One)
def UInt(n): return Zero if n == 0 else Succ(UInt(n-1))
PairNPlus1N = lambda p: Pair(Succ(First(p)))(First(p))
Prev = lambda x: Second(x(PairNPlus1N)(Pair(Zero)(Zero)))

# arithmetic
Add = lambda x: lambda y: x(Succ)(y)
Multiply = lambda x: lambda y: lambda z: x(y(z))

# cmp
IsZero = lambda x: x(F)(Not)(F)
GreaterEqual = lambda x: lambda y: IsZero(x(Prev)(y))
LessEqual = lambda x: lambda y: IsZero(y(Prev)(x))
Equal = lambda x: lambda y: And(GreaterEqual(x)(y))(LessEqual(x)(y))
NotEqual = lambda x: lambda y: Not(Equal(x)(y))
Greater = lambda x: lambda y: IsZero(x(Prev)(Succ(y)))
Less = lambda x: lambda y: IsZero(y(Prev)(Succ(x)))