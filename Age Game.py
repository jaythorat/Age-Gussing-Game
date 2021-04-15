min_age = 1
max_age = 150
print("Your age should be in {} to {}".format(min_age,max_age))
input("Press Enter to start the game!!")
guesses = 1
while True :
    guess = min_age + (max_age - min_age) // 2
    max_min = input("""Are you {} years old? 
                    A : Less
                    B : More
                    C : Correct
                    --->""".format(guess)).casefold()
    if max_min == "a" :
        max_age = guess - 1
    elif max_min == "b" :
        min_age = guess +1
    elif max_min == "c" :
        print("Yaay!!! I got you right.. Guessed you age in {} tries :)".format(guesses))
        break
    else:
        print("Please enter valid choice A,B or C")
    guesses += 1