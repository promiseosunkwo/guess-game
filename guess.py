import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too low (L), too high (H), correct (C)').lower()
        if feedback == 'h':
           high = guess - 1
        elif feedback == 'l':
           high = guess + 1
    print("Yeayyy! Computer has the correct answer")

computer_guess(10000)

# def guess(x):
#     random_number = random.randint(1, x)
#     guess_number = 0
#     while random_number != guess_number:
#         guess_number = int(input("Enter a number: " ))
#         if(guess_number > random_number):
#             print("Sorry too high, Try again!")
#         elif(guess_number < random_number):
#             print("Sorry too low, Try again!")
#     print("Yaaaah! you got the number! Well done")


# guess(3000)


