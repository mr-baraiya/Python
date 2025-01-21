# [1,2,2,3,4,4,5,6,6] => [1,2,3,4,5,6]

# l = [1,2,2,3,4,4,5,6,6]
# s = set(l)
# l = list(s)
# l.sort()    
# print(l)

l = [1,2,2,3,4,4,5,6,6,6,7,8,5,4,3,2,34,6,43,4]
l.sort()
for i in l:
    idx = l.index(i)
    if l.count(i) > 1:
        for j in range(0,l.count(i)):
            l.remove(i)
        l.insert(idx,i)
    else:
        pass
        
print(l)