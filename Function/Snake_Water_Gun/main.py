import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s , w , g): ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

# Ny now we have 2 numbers (variables), you and computer
print(f"Computer choose {reverseDict[computer]} and \nYou choose {reverseDict[you]}.")

if (computer == you):
    print("It's Draw!")
elif(computer == -1 and you == 1):
    print("You Win!")
elif(computer == -1 and you == 0):
    print("You loos!")
elif(computer == 1 and you == -1):
    print("You loos!")
elif(computer == 1 and you == 0):
    print("You win!")
elif(computer == 0 and you == 1):
    print("You loos!")
elif(computer == 0 and you == -1):
    print("You win!")
else:
    print("Somethinn went wrong!")
