module Main where 

import Test.HUnit
import qualified Utils
import qualified Boolean

tests = TestList [Utils.tests, Boolean.tests]

main = do
    runTestTT tests
