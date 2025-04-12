def isArmstrong(n):
    sum = 0
    length = len(str(n))
    a = n
    while n != 0:
        sum = sum + ((n % 10) ** length)
        n = n // 10
        
    if a == sum:
        return 1
    else:
        return 0
    
n = int(input("Enter the number : "))
if isArmstrong(n) == 1:
    print(f"{n} is Armstrong number.")
else:
    print(f"{n} is Not Armstrong number.")