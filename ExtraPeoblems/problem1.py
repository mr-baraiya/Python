# [1,3,9,2,5,4,3,2,1] => [9,5,4,3,2,1]
l = [1,3,9,2,5,4,3,2,1]
l1 = []
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i] < l[j]:
            break
    else:
        l1.append(l[i])
print(l1)