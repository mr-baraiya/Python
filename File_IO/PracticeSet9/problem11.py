import os

with open("file2.txt") as f:
    content = f.read()
    
with open("renamed_by_python.txt","w") as f:
    f.write(content)
    
os.remove("file2.txt")