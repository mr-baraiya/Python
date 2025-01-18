myList = [1,2,3,4,5,6,7,8,9,10]

newList = [i**2 for i in myList]
print(newList)


newDict = {i : i**2 for i in myList}
print(newDict)