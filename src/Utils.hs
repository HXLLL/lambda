module Utils where

import Test.HUnit

-- pair
pair = \x -> \y -> \f -> f x y
first = \p -> p (\x -> \y -> x)
second = \p -> p (\x -> \y -> y)

-- utils
realPair = \p -> (first p, second p)

-- tests
tests = "Utils" ~: TestList ["pair" ~: (realPair (pair 1 2)) ~?= (1,2)]
