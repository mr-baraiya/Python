class Demo:
    a = 4
    
n = Demo()
print(n.a) # Prints The Class Attribute beacause instance Attribute is not present
n.a = 0
print(n.a) # Prints Te instance Attribute present
print(Demo().a) # prints The class atribute