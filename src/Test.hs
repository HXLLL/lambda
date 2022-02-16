module Main where 

import System.Exit (exitFailure)
import Test.HUnit
import qualified Utils
import qualified Boolean

tests = TestList [Boolean.tests]

main = do
    runTestTT tests
    exitFailure
