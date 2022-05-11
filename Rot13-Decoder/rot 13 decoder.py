def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "a":
            if letter.isupper():
                translation = translation + "N"
            else:
                translation = translation + "n"

        elif letter.lower() in "b":
            if letter.isupper():
                translation = translation + "O"
            else:
                translation = translation + "o"

        elif letter.lower() in "c":
            if letter.isupper():
                translation = translation + "P"
            else:
                translation = translation + "p"

        elif letter.lower() in "d":
            if letter.isupper():
                translation = translation + "Q"
            else:
                translation = translation + "q"

        elif letter.lower() in "e":
            if letter.isupper():
                translation = translation + "R"
            else:
                translation = translation + "r"


        elif letter.lower() in "f":
            if letter.isupper():
                translation = translation + "S"
            else:
                translation = translation + "s"

        elif letter.lower() in "g":
            if letter.isupper():
                translation = translation + "T"
            else:
                translation = translation + "t"

        elif letter.lower() in "h":
            if letter.isupper():
                translation = translation + "U"
            else:
                translation = translation + "u"

        elif letter.lower() in "i":
            if letter.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"

        elif letter.lower() in "j":
            if letter.isupper():
                translation = translation + "W"
            else:
                translation = translation + "w"

        elif letter.lower() in "k":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"

        elif letter.lower() in "l":
            if letter.isupper():
                translation = translation + "Y"
            else:
                translation = translation + "y"

        elif letter.lower() in "m":
            if letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"   

        elif letter.lower() in "n":
            if letter.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"

        elif letter.lower() in "o":
            if letter.isupper():
                translation = translation + "B"
            else:
                translation = translation + "b"

        elif letter.lower() in "p":
            if letter.isupper():
                translation = translation + "C"
            else:
                translation = translation + "c"

        elif letter.lower() in "q":
            if letter.isupper():
                translation = translation + "D"
            else:
                translation = translation + "d"

        elif letter.lower() in "r":
            if letter.isupper():
                translation = translation + "e"
            else:
                translation = translation + "E"


        elif letter.lower() in "s":
            if letter.isupper():
                translation = translation + "F"
            else:
                translation = translation + "f"

        elif letter.lower() in "t":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "H"
            else:
                translation = translation + "h"

        elif letter.lower() in "v":
            if letter.isupper():
                translation = translation + "I"
            else:
                translation = translation + "i"

        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + "j"

        elif letter.lower() in "x":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"

        elif letter.lower() in "y":
            if letter.isupper():
                translation = translation + "L"
            else:
                translation = translation + "l"

        elif letter.lower() in "z":
            if letter.isupper():
                translation = translation + "M"
            else:
                translation = translation + "m"
    print(translation)

translate(input("Enter a phrase: "))







