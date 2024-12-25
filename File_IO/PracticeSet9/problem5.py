words = ["Monkey","Donkey","good"]
word = "Donkey"
with open("dunki.txt","r") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word,"#"*len(word))
    
with open("dunki.txt","w") as f:
    f.write(content)