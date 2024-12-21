# def printName(name,ends):
#     print("Your Name : ",name)
#     print(ends)
    
# name = input("Enter your Name : ")
# printName(name,"Thank You")

# name = input("Enter your Name : ")
# printName(name,"Thanks")

def concateWithHello(name):
    name = "Hello "+ name
    return name

name = "Tony"
updatedName = concateWithHello(name)
print(updatedName)