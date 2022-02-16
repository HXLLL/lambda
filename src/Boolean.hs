module Boolean where 

import Unsafe.Coerce
import Test.HUnit
import Utils
import TestUtils

-- boolean algebra
true :: p -> p -> p
true = \x -> \y -> x
false :: p -> p -> p
false = \x -> \y -> y

inv :: p -> p
inv = \x -> unsafeCoerce x false true

and :: p -> p -> p
and = \x -> \y -> unsafeCoerce x y false

or :: p -> p -> p
or = \x -> \y -> unsafeCoerce x true y

-- utils
-- toBool :: t -> Bool
toBool b = b True False

-- toMyBool :: Bool -> t
toMyBool True = true
toMyBool False = false

-- tests

boolBinaryTests my_op std_op = 
  binaryTests boolRanges my_op std_op toMyBool toBool

tests = "Boolean" ~: test [
            "true" ~: toBool true ~?= True
          , "false" ~: toBool false ~?= False
          , "not" ~: unaryTests boolRanges inv not toMyBool toBool
          , "and" ~: boolBinaryTests Boolean.and (&&)
          , "or" ~: boolBinaryTests Boolean.or (||)
          ]