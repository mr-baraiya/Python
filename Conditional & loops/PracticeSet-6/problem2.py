sub1 = int(input("Enter the marks of Subject 1 :"))
sub2 = int(input("Enter the marks of Subject 2 :"))
sub3 = int(input("Enter the marks of Subject 3 :"))

per = ((sub1 + sub2 + sub3)/300)*100


if(per >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You are Passed",per)
else:
    print("Failed")