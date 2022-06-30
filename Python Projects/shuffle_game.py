import random

def shuffle_list(li):
    random.shuffle(li)
    return li



def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:

     guess = input("Pick a Position: ")

    return int(guess)


def game_checker(li, guess):

    if li[guess] == "O":
        print("Correct")
    else:
        print("Sorry, wrong")
        print(li)

def main():
    game_list = [" ", "O", " "]

    shuffled = shuffle_list(game_list)

    player = player_guess()

    game_checker(shuffled,player)


print(main())
