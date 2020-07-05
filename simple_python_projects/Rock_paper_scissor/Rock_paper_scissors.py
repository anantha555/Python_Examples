import random
options = ["r","p","s"]
draw = "It's a Draw this Round"
compWin ="Computer Wins this Round"
humanWin ="You Win this Round" 
humanScore , computerScore , tie  = 0,0,0
game = "START"


def rps(h,c): 

  if h == "p" and c == "p":
    return draw
  elif h == "r" and c == "r":
    return draw
  elif h == "s" and c == "s":
    return draw
  elif h == "p" and c == "s":
    return compWin
  elif h == "p" and c == "r":
    return humanWin
  elif h == "r" and c == "s":
    return humanWin
  elif h == "r" and c == "p":
    return compWin
  elif h == "s" and c == "r":
    return compWin
  elif h == "s" and c == "p":
    return humanWin
 
while game == "START":
  result =""
  humanInput = input("\nEnter Choice (r/p/s) to Play or (exit) to Stop Playing:\n")
  print("Your choice is:", humanInput)
  if humanInput.lower() == "p" or humanInput.lower() == "r" or humanInput.lower() =="s":
    computerChoice = random.choice(options)
    print("computer choice is:", computerChoice,"\n\n")
    result = rps(humanInput.lower(),computerChoice)
    print("Result:",result,"\n")
    if result == compWin:
      computerScore += 1
    elif result == humanWin:
      humanScore +=1
    elif result == draw:
      tie +=1
    print("Game Board \nHuman:",humanScore,"\nComputer:",computerScore,"\nTies:",tie)

  elif humanInput.lower() == "exit":
    game = "STOP"
    if humanScore > computerScore:
      print("You Win the Match! Congratulations !")
    elif computerScore > humanScore:
      print("Computer Wins the Match , Better Luck Next Time !") 
    elif (computerScore == humanScore != 0) :#and (tie != 0 or tie == 0):
      print("Scores Equal, Its a Draw Match !")
    elif computerScore == humanScore == 0 and tie == 0:
      print("Match Ended Without Play")
    elif computerScore == humanScore == 0 and tie != 0:
      print("Both Scores = 0, Its a Draw Match !") 
    #print(game)
    #result =""
    #break
  elif humanInput.lower() != "p" or "r" or "s"  or "exit":
    #game ="START"
    #result =""
    print("Invaild Input Try Again")
