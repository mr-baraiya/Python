f = open("file.txt")

# F.ReadLines()
# lines = f.readlines()
# print(lines,type(lines))

# f.readLine()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(line1,line2,line3,line4)
# f.close()
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
    
f.close()