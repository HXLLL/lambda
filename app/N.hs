
zero = \x -> \y -> y
nxt = \x -> \f -> \y -> f (x f y)
one = nxt zero
two = nxt one
add = \x -> \y -> x nxt y
