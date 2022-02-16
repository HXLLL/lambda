module TestUtils where

import Test.HUnit

-- unaryTests :: (Eq a, Show a) => 
-- inputF: convert built-in values to lambda calculus
-- outputF: convert lambda calculus to built-in values
unaryTests range inputF outputF my_op std_op = test [
  "op " ++ (show x) ~:
  (outputF (my_op (inputF x))) ~?= (std_op x) | x <- range]

-- binaryTests :: (Eq a, Show a) => 
-- inputF: convert built-in values to lambda calculus
-- outputF: convert lambda calculus to built-in values
binaryTests range inputF outputF my_op std_op = test [
  (show x) ++ " op " ++ (show y) ~: 
  (outputF (my_op (inputF x) (inputF y))) ~?= (std_op x y) 
    | x <- range, y <- range]