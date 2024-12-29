class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class Attribute of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.sname}"


    @name.setter 
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.sname = value.split(" ")[1]
        
e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.name)
print(e.fname,e.sname,sep=",")