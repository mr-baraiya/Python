class Employee:
    name = "Tony"
    Salary = 12000
    
    def __init__(self):
        print("This is Employee Constucter.")
        
    def show(self):
        print(f"The name is {self.name} and Salary is {self.salary}.")
            
class Devloper(Employee):
    company = "InfoTech"
    
    def __init__(self):
        super().__init__()
        print("This is Devloper Constucter.")
        
    def showLanguage(self):
        print(f"{self.language} is the best language")
    
e = Employee()

d = Devloper()