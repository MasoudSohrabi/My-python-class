import random

print("rock")
print("paper")
print("scissors")

randomMove = random.randint(0 , 2)

cpuMove = "rock"

if randomMove == 0:
    cpuMove = "rock"
elif randomMove == 1:
    cpuMove = "paper" 
elif randomMove == 2:
    cpuMove = "scissors"    
    
    
Player_1 = input("Player_1 , make your move:").lower()
print(f"Player_2 make your move: {cpuMove}")
Player_2 = cpuMove
       

if Player_1 == Player_2:
    print("draw!")
elif Player_1 == "rock":
    if Player_2 =="scissors":
        print("Player_1 wins!")
    elif Player_2 == "paper":
        print("Player_2 wins!")    
elif Player_1 == "paper":
    if Player_2 == "rock":
        print("Player_1 wins!")
    elif Player_2 == "scissors":
        print("Player_2 wins!")
elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("Player_1 wins!")
    elif Player_2 == "rock":
        print("Player_2 wins!")
else: 
    print("one of you input wrong option!")                        
    