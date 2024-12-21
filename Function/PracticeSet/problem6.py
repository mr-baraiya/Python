def inchesToCms(inch):
    return inch * 2.54

n = int(input("Enter the value in inches : "))
print(f"{n} inches = {inchesToCms(n)} cms")