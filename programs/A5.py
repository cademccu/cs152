# Rock Paper Scissors Lizard Spock

from random import choice,seed

def computer_player():
    '''return a random selection from the 5 options.'''
    return choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


def human_player():
    '''prompt and return a human selection from the 5 options.'''
    return str(input("rock, paper, scissors, lizard, or spock?\n"))

def outcome(p1, p2):
    '''return win, lose, or draw for the player1.'''
    if p1 == p2:
        return "draw"
    elif p1 == "lizard":
        if p2 == "spock" or p2 == "paper":
            return "win"
    elif p1 == "paper":
        if p2 == "rock" or p2 == "spock":
            return "win"
    elif p1 == "rock":
        if p2 == "lizard" or p2 == "scissors":
            return "win"
    elif p1 == "scissors":
        if p2 == "lizard" or p2 == "paper":
            return "win"
    elif p1 == "spock":
        if p2 == "rock" or p2 == "scissors":
            return "win"
    return "lose"


def main():
    # determine player choices
    human = human_player()
    computer = computer_player()
    # print human outcome computer
    print(human, outcome(human,computer), computer)
    

# Do not modify the following code or your tests will fail.
if __name__ == '__main__':
    seed(42)
    main()
