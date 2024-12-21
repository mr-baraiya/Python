
def celciusToFarehenhit(temp=0):
    return (((temp // 5.0) * 9) + 32)

temp = int(input("Enter the temprature : "))
f = celciusToFarehenhit(temp)
print(f"Temprature : {round(f,2)} Degree Celcius")