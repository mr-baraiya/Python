n = int(input("Enter the numebr :"))

for i in range(2,(n//2+1)):
    if(n%i == 0):
        print("Number is Not Prime")
        break
else:
    print("Number is Prime")