# # tuple is immutable but list are amutable.
# # it is tuple a = (1) it is int
# a = (1,2,3,4,5) 
# a = (1,) 
# #it is tuple in which only one elemant exist
# name = (1,23,45.67,"Nayan")
# print(name)
# # a[0] = "Vishal" you can not do that

a = (1,23,45,67.89,False,"Rohan")
print(a)
no = a.count(45)
print(no)
index = a.index("Rohan")
print(index)
