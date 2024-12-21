n1 = int(input("Enter the Number : "))
n2 = int(input("Enter the Number : "))
n3 = int(input("Enter the Number : "))

def max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
print(max(n1,n2,n3))