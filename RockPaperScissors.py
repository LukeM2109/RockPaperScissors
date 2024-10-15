import random

comp_score = 0
user_score = 0

while comp_score or user_score != 3:
    answer = input("Enter Rock, Paper or Scissors: ")
    number = random.randint(1, 3) # 1 is rock, 2 is Paper, 3 is Scissors
    
     # Rock Solutions 
    
    if number == 1 and answer == "Rock":
        print("Draw! Rock and Rock")
        print("Your Score:", user_score, "Computer Score:", comp_score)
    elif number == 1 and answer != "Paper" and "Rock":
        print("You lose. Rock beats Scissors")
        comp_score = comp_score + 1
        print("Your Score:", user_score, "Computer Score:", comp_score)
    elif number == 1 and answer == "Paper":
        print("You win. Paper beats Rock.")
        user_score = user_score + 1
        print("Your Score:", user_score, "Computer Score:", comp_score)
        
    # Paper Solutions
        
    if number == 2 and answer == "Paper":
        print("Draw! Paper and Paper")
        print("Your Score:", user_score, "Computer Score:", comp_score)
    elif number == 2 and answer != "Paper" and "Scissors":
        print("You lose! Paper beats Rock ")
        comp_score = comp_score + 1
        print("Your Score:", user_score, "Computer Score:", comp_score)
    elif number == 2 and answer == "Scissors":
        print("You win! Scissors beats Paper")
        user_score = user_score + 1
        print("Your Score:", user_score, "Computer Score:", comp_score)
        
    # Scissors Solutions
    
    if number == 3 and answer == "Scissors":
        print("Draw! Scissors and Scissors")
        print("Your Score:", user_score, "Computer Score:", comp_score)
    elif number == 3 and answer != "Scissors" and "Rock":
        print("You lose! Scissors beats Paper ")
        comp_score = comp_score + 1
        print("Your Score:", user_score, " Computer Score:", comp_score)
    elif number == 3 and answer == "Rock":
        print("You win! Rock beats Paper")
        user_score = user_score + 1
        print("Your Score:", user_score, " Computer Score:", comp_score)
    
    if comp_score or user_score == 3:
        break;
        
