with open("demo.txt") as f:
    content = f.read()
    
if ("twinkle" in content):
    print("Twinkle is present in Content")
else:
    print("Twinkle is Not present in Content")
    
f.close()