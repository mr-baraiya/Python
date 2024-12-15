# friends = ["Apple","Orange",5,90.78,True]
# print(friends)
# print(friends[2])
# print(friends[1:4])
# friends.append("Darshan")
# print(friends)

l1 = [12,45,21,34,89,67,54,2]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,90) # At index 3 inserted 90
print(l1)
a = l1.pop(3) # At index 3 removed
print(a," was removed from ",l1)
a = l1.remove(34) # remove 34
print(a," was removed from ",l1)