def my_encrypt():
    x = input("Enter a word\n")
    y = list(x)
    total = ""
    for i in y:
        if i == "A" or i == "a":
            i = "?"
        elif i == "B" or i == "b":
            i = "."
        elif i == "C" or i == "c":
            i = ","
        elif i == "D" or i == "d":
            i = "-"
        elif i == "E" or i == "e":
            i = "_"
        elif i == "F" or i == "f":
            i = "#"
        elif i == "G" or i == "g":
            i = "$"
        elif i == "H" or i == "h":
            i = "^"
        elif i == "I" or i == "i":
            i = "&"
        elif i == "J" or i == "j":
            i = "*"
        elif i == "K" or i == "k":
            i = "@"
        elif i == "L" or i == "l":
            i = "~"
        elif i == "M" or i == "m":
            i = "("
        elif i == "N" or i == "n":
            i = "="
        elif i == "O" or i == "o":
            i = "+"
        elif i == "P" or i == "p":
            i = ">"
        elif i == "Q" or i == "q":
            i = "/"
        elif i == "R" or i == "r":
            i = "}"
        elif i == "S" or i == "s":
            i = ":"
        elif i == "T" or i == "t":
            i = "|"
        elif i == "U" or i == "u":
            i = ";"
        elif i == "V" or i == "v":
            i = "'"
        elif i == "W" or i == "w":
            i = "%"
        elif i == "X" or i == "x":
            i = "["
        elif i == "Y" or i == "y":
            i = "]"
        elif i == "Z" or i == "z":
            i = ")"

        total = total + i
    return total




print(my_encrypt())