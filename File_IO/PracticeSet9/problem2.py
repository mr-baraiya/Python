import random
def Game():
    print("You are playing the game... ")
    score = random.randint(1,62)
    print(f"Your Score : {score}")
    # fetch the hi-Score
    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    if (score > hiscore or hiscore ==""):
         with open("Hi-score.txt","w") as f:
             hiscore = f.write(str(score))
    return score

Game()