# pair
Pair = lambda x: lambda y: lambda z: z(x)(y)
First = lambda p: p(lambda x: lambda y: x)
Second = lambda p: p(lambda x: lambda y: y)

# boolean algebra
T = lambda x: lambda y: x
F = lambda x: lambda y: y
def Boolean(b): return T if b else F
Not = lambda x: x(F)(T)
And = lambda x: lambda y: x(y)(F)
Or = lambda x: lambda y: x(T)(y)

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

# cond
Cond = lambda x: lambda y: lambda z: x(y)(z)

# cmp
IsZero = lambda x: x(F)(Not)(F)
GreaterEqual = lambda x: lambda y: IsZero()

# Integer
Minus = lambda x: 
