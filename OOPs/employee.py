class Employee:
    language = "Python"
    salary = 12000
    
    def getInfo(self):
        print(f"Language is {self.language}.")
        print(f"Salary is {self.salary}.")
    
    @staticmethod
    def greet():
        print("Hello!")
        
harry = Employee()
harry.getInfo()
harry.greet()