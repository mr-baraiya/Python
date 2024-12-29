class Employee:
    language = "Python"
    salary = 120000
    
    def __init__(self,name,salary,language): # dunder method which automatically called
        print("Object Was Created.")
        self.language = language
        self.name = name
        self.salary = salary
        
harry = Employee("Harry",13000,"Javascript")
print(f"{harry.name} , {harry.language} , {harry.salary}")