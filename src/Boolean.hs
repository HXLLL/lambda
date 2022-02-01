module Boolean where 

import Test.HUnit

-- boolean algebra
true = \x -> \y -> x
false = \x -> \y -> y
inv = \x -> x false true
and = \x -> \y -> x y false
or = \x -> \y -> x true y

-- utils
realBool :: t -> Bool
realBool true = True
realBool false = False

tests = "Boolean" ~: test ["true" ~: realBool true ~?= True,
                           "false" ~: realBool false ~?= False,
                           ]
