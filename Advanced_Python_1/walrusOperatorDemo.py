# Usin walrus Operator
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too Long ({n} elemants, expected <= 3)")