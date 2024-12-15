# It is Dictionary
# In is unOrdered
# Cannot contains duplicate value
# it is mutable
marks = {
    "Harsh" : 100,
    "Vishal" : 45,
    "Darshan" : 34,
    56 : "Vishal"
}
print(marks)
print(type(marks))
print(marks["Vishal"])
print()

print(marks.items()) # it returns a list of markes
print(marks.keys())
print(marks.values())

marks.update({"Harsh": 99 , "Renuka": 67})
print(marks)

print(marks.get("Shivika"))
print(marks.get("Vishal")) # If not exist the return none
print(marks["Vishal"]) # return Error

marks.clear() # clear dictionary
print(marks)
print(len(marks))