from random import randrange


def get_computer_choice():
    computer = randrange(3)
    if computer == 0:
        return "rock"
    elif computer == 1:
        return "paper"
    elif computer == 2:
        return "scissors"
    else:
        print("problem with get_computer_choice() function !")
        return "NULL"


def get_human_choice():
    human_input = input("Enter rock, paper or scissors: ")
    human_input = human_input.lower()
    if human_input == "rock":
        return human_input
    elif human_input == "paper":
        return human_input
    elif human_input == "scissors":
        return human_input
    else:
        print("Please write the exact word (case insensitive) : 'rock', 'paper' or 'scissors' !")
        get_human_choice()


def game_welcome():
    print("Welcome to the paper rock scissors game")
    print("The game has 5 rounds except in case of a tie. If a round has a tie, the game is incremented by 1")
    input("Are you ready ? Please type something to continue: ")


def game():
    game_welcome()
    i = 0; score = 0; computer_win = 0; human_win = 0
    while i < 5:
        computer = get_computer_choice(); human = get_human_choice()
        if computer == human:
            i -= 1; score += 1
            print(f'Equality ! Computer plays {computer} and Player plays {human} - score : Computer = 0 and Player = 0')
        elif (computer == "rock" and human == "scissors") or (computer == "paper" and human == "rock") or (computer == "scissors" and human == "paper"):
            computer_win += 1; score += 1
            print(f'Computer wins ! Computer plays {computer} and Player plays {human} - score : Computer = 1 and Player = 0')
        elif (human == "rock" and computer == "scissors") or (human == "paper" and computer == "rock") or (human == "scissors" and computer == "paper"):
            human_win += 1; score += 1
            print(f'Player wins ! Computer plays {computer} and Player plays {human} - score : Computer = 0 and Player = 1')
        else:
            print("Problem with game() function !")
        i += 1
    if computer_win > human_win:
        winner = "Computer"
    elif computer_win < human_win:
        winner = "Player"
    print(f'End of the game ! - The game has {score} parts - Computer haves {computer_win} points and Player haves {human_win} points - The winner is {winner}')



game()