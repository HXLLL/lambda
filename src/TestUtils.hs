module TestUtils where

import Test.HUnit

boolRanges = [True, False]
naturalNumberRanges = [1..10]

-- unaryTests :: (Eq a, Show a) => 
--  [a] -> (t->t) -> (a->a) -> (a->t) -> (t->a) -> Test
-- inputF: convert built-in values to lambda calculus
-- outputF: convert lambda calculus to built-in values
unaryTests range my_op std_op inputF outputF = test [
  "op " ++ (show x) ~:
  (outputF (my_op (inputF x))) ~?= (std_op x) | x <- range]

-- binaryTests :: (Eq a, Show a) => 
--   [a] -> (t->t->t) -> (a->a->a) -> (a->t) -> (t->a) -> Test
-- inputF: convert built-in values to lambda calculus
-- outputF: convert lambda calculus to built-in values
binaryTests range my_op std_op inputF outputF = test [
  (show x) ++ " op " ++ (show y) ~: 
  (outputF (my_op (inputF x) (inputF y))) ~?= (std_op x y) 
    | x <- range, y <- range]