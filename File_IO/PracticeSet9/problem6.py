with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes Python is Present in Log.txt")
else:
    print("Not Python is Not Present in Log.txt")