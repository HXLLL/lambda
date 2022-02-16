module Main where 

import System.Exit (exitFailure)
import Test.HUnit
import qualified Utils
import qualified Boolean
import qualified NaturalNumber as N

tests = TestList [ Boolean.tests
                 , N.tests ]

main = do
    runTestTT tests
    exitFailure
