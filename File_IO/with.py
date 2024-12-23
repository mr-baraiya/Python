# f = open("file.txt")
# print(f.read())
# f.close()
# this same work we do it with 'with' Statement

with open("file.txt") as f:
    print(f.read())
    