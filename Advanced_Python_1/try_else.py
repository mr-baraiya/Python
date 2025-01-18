try:
    n = int(input("Enter the Number : "))
    print(n)
    
except Exception as e:
    print(e)
    
else:
    print("I am Inside Else") # if Exception Will Not Come the Else Block will Execute