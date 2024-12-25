line = 1
with open("log.txt") as f:
    content = f.readlines()
    
for text in content:
    if("python" in text):
        print(f"Python is present in {line}.")
        break
    line += 1
    
else:
    print(f"Python is Not present.")