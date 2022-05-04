import random
while True:
    top_range=input("Enter a upper limit:")
    if top_range.isdigit():
        top_range=int(top_range)
        if top_range<=10:
            print("Please type a number greater than 10")
            continue
        break
    else :
        print("Please type a number")
random_number=random.randint(0,top_range)
guesses=0
while True:
    guesses+=1
    while True:
        user_guess=input("Make a guess:")
        if user_guess.isdigit():
            user_guess=int(user_guess)
            break
        else:
            print("Please enter a number")
            continue
    if user_guess==random_number:
        print("You got it!")
        break
    elif user_guess<random_number:
        print("You were below the number")
    else :
        print("You were above the number")
print("You got it in",guesses,"guesses.")


