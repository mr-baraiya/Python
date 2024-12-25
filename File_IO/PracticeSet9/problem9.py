with open("this.txt") as f:
    content1 = f.read()
    
with open("copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes This file are Identical.")
else:
    print("No these file not a identical.")
