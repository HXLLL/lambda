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

# cond
Cond = lambda x: lambda y: lambda z: x(y)(z)

Y = lambda y: (lambda x: y(x(x)))(lambda x: y(x(x)))
