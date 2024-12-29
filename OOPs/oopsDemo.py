class Employee:
    # Here is a class Attribute
    language = "python"
    Salary = "12000"

harry = Employee()
print(harry.Salary,harry.language)

# Here name is a object Attribute and instance attribute
rohan = Employee()
rohan.name = "Rohan Arora"
print(rohan.name,rohan.Salary,rohan.language)

Lalu = Employee()
Lalu.name = "Lalu"
Lalu.language = "Java"
print(Lalu.name,Lalu.Salary,Lalu.language)