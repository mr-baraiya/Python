f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content.")
    
f.close()