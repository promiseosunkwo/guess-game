import random

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while random_number != guess_number:
        guess_number = int(input("Enter a number: " ))
        if(guess_number > random_number):
            print("Sorry too high, Try again!")
        elif(guess_number < random_number):
            print("Sorry too low, Try again!")
    print("Yaaaah! you got the number! Well done")


guess(3000)
