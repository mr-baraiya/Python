word = "Donkey"
with open("dunki.txt","r") as f:
    content = f.read()
    
with open("dunki.txt","w") as f:
    content = content.replace("Donkey","######")
    f.write(content)
    
