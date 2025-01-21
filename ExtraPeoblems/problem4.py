# n = 123456 => 21 => 3
n = 123456
s = str(n)
while(len(s) != 1):
    sum = 0
    for i in s:
        sum += int(i)
        s = str(sum)

n = int(s)
print(n)