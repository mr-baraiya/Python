# [0,-2,1,0,3,9,7,0,4] => [-2,1,3,9,7,4,0,0,0]
l = [0,-2,1,0,3,9,7,0,4]
for i in l:
    if i == 0:
        l.remove(i)
        l.append(0)
        
print(l)