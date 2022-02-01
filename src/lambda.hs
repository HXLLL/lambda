type Label = Int
data Expression = Lambda Label Expression | Var Label

Zero = Lambda 1 

main = do
    print("Hello")
