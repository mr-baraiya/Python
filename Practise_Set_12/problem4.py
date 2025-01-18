try:
    a = int(input("Enter the First Number : "))
    b = int(input("Enetr the Second  Number : "))
    print(f"{a} / {b} = {a/b}")
    
except ZeroDivisionError as z:
    print("Infinite")