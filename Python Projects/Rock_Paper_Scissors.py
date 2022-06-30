import random

def player_guess():
    x = input("Choose rock, paper, or scissor: ")

    return x

def computer_choice():
    li = ["rock", "paper", "scissor"]
    comp = random.choice(li)

    return comp

def decider(x, comp):
    if x == "rock" and comp == "scissocr" or x == "paper" and comp == "rock" or x == "scissor" and comp == "paper":
        print("You Win!")
        print(comp)
    elif x == comp:
        print("Tie!")
        print(comp)
    else:
        print("You loose")
        print(comp)

def main():
    computer = computer_choice()

    player = player_guess()

    decider(computer, player)

print(main())


