import random

def number_guess ():
    con = "yes"
    while con == "yes" or "Yes":

        rand = random.randint(0,1000)
        user = int(input("Enter a number 0-1000 \n"))

        if user == rand:
            print("You Win!")
        else:
            print("You lose")

        con = input("Would you like to continue? \n")


print(number_guess())