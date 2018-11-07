'''
documentation
***********
'''

import random

secret = random.randint(1,99)

guess = 0
tries = 0
print("can you guess my number?")
print("my number is an intenger between 1 and 99")


while guess != secret and tries > 6:
    print("hey what is your guess?")
    guess = int(input)
    if guess > secret :
        print("to low !")
    elif guess > secret :
        print("too high!")
    tries = tries + 1


if guess == secret :
    print("you got it!")
else :
    print("no more guesses! try again!")
    print("the secret number is : ", secret)