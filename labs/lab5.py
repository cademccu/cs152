# Rock Paper Scissors

from random import choice,seed

choices = ['rock','paper','scissors']

def computer_player():
    '''return a random selection from the 3 options.
    DO NOT CHANGE THIS CODE'''
    return choice(choices)


def human_player():
    '''prompt and return a human selection from the 3 options.'''
    return str(input("rock, paper, or scissors?\n"))
    
    
def outcome(player1, player2):
    '''return win, lose, or draw for the player1.'''

    if player1 == player2:
        return "draw"
    elif player1 == "rock":
        return "win" if (player2 == "scissors") else "lose"
    elif player1 == "scissors":
        return "win" if (player2 == "paper") else "lose"
    else: # paper
        return "win" if (player2 == "rock") else "lose" 

def main():
    # determine player choices
    human = human_player()
    computer = computer_player()
    # print human outcome computer
    print(human, outcome(human,computer), computer)
    
    


# Do not modify the following code or your tests will fail.
'''DO NOT CHANGE THIS CODE'''
if __name__ == '__main__':
    seed(42)
    main()
