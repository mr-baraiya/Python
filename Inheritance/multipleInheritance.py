class Employee:
    def show(self):
        print(f"The name is {self.name} and Salary is {self.salary}.")
    
class Coder:
    language = "Python"
    
    def showLanguage(self):
        print(f"{self.language} is the best language")
        
class Devloper(Employee , Coder):
    company = "InfoTech"
    
d = Devloper()
d.name = "Tony"
d.salary = 150000
d.language = "python"
d.show()
d.showLanguage()
