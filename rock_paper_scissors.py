import random

print ("rock...")
print ("paper...")
print ("scissors...")
print ("Welcome to rock, paper, scissors, smackdown!!!")
print ("What is your name?")

name = input()
player = input( name + ", select rock, paper, or scissors to make your move:") 


rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

	
print (f"Computer plays {computer}")

if player == "rock" and computer == "scissors":
	print(name + " wins!")
elif player == "rock" and computer == "paper":
	print("computer wins!")
elif player == "rock" and computer == "rock":
	print("It's a tie!")
elif player == "scissors" and computer == "rock":
	print("computer wins!") 
elif player == "scissors" and computer == "paper":
	print(name + " wins!") 
elif player == "scissors" and computer == "scissors":
	print("It's a tie!") 
elif player == "paper" and computer == "rock":
	print(name + " wins!") 
elif player == "paper" and computer == "scissors":
	print("computer wins!") 
elif player == "paper" and computer == "paper":
	print("It's a tie!")

else:
	print("something went wrong")
