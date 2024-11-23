light = input("light : ")

if light.lower() == "red" :
    print("stop")
elif light.lower() == "yellow" :
    print("look")
elif light.lower() == "green" :
    print("go")
else :
    print("light is broken")
    
# below line is execute for all condition
print("jk") 
# ternory operator

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet") 

#Clever if Ternary Operator
age = int(input("age : "))
vote = ("yes","no") [age < 18]
print(vote)