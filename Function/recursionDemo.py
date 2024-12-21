# fact(5) = 5 * fact(4)
# fact(4) = 4 * fact(3)
# fact(3) = 3 * fact(2)
# fact(2) = 2 * fact(1)
# fact(1) = 1 * fact(0)
# fact(0) = 1
def fact(n):
    if(n == 1 or n==0):
        return 1
    else:
        return n * fact( n-1 )
    
n = int(input("Enter the Number : "))
print(f"Factorial of {n} = {fact(n)}")
     