class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pinCode):
        self.name = name
        self.salary = salary
        self.pinCode = pinCode
        
p = Programmer("Tony Stark",12000,123456)
print(f" Company : {p.company} \n name : {p.name} \n Salary : {p.salary} \n PinCode : {p.pinCode}")