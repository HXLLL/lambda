module NaturalNumber where 

import Unsafe.Coerce
import Test.HUnit
import Utils
import TestUtils

zero :: a -> b -> b
zero = \x -> \y -> y

nxt :: a -> a
nxt = \x -> \f -> \y -> unsafeCoerce f (x f y)
one = nxt zero
two = nxt one
add = \x -> \y -> x nxt y

-- utils
toInt n = n (+1) 0

-- toMyInt :: Int -> p
-- toMyInt 0 = zero
-- toMyInt n = nxt (toMyInt (n-1))

-- tests

natRange = [0..10]

-- natBinaryTest = 
--   binaryTests natRange toMyInt toInt

tests = "NaturalNumber" ~: test [
            "zero" ~: toInt zero ~?= 0
          , "one" ~: toInt one ~?= 1
          , "two" ~: toInt two ~?= 2
          ]