class Calculater:
    
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"Square is : {self.n ** 2}")
    def cube(self):
        print(f"Cube is : {self.n ** 3}")
    def squareRoot(self):
        print(f"Square Root : {self.n ** (1/2)}")
    
    @staticmethod
    def hello():
        print("Hello there!")
        
a = Calculater(4)
a.square()
a.cube()
a.squareRoot()
a.hello()