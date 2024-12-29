class Employee:
    def show(self):
        print(f"The name is {self.name} and Salary is {self.salary}.")
            
class Devloper(Employee):
    company = "InfoTech"
    
    def showLanguage(self):
        print(f"{self.language} is the best language")
    
e = Employee()
e.name = "Harry"
e.salary = 120000
e.show()

d = Devloper()
d.name = "Tony"
d.salary = 150000
d.language = "python"
d.show()
d.showLanguage()
