#Pyhton Project #2: Guess the Number from Computer
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from random import randint
from time import sleep

#Declaring the variables
user_number = ""
cpu_guess = ""
feedback = ""
low = 1
high = 1000
not_guessed = True

#Program
print("GUESS MY NUMBER GAME!\n")
sleep(1)

user_number = int(input("Enter a random number: "))
print("Let's see of the computer can guess your number...\n")
sleep(2)

#Ask the user to try a first guess
while not_guessed:

    #Condition to prevent error code
    if low != high:
        cpu_guess = randint(low, high)
    else:
        guess = low

    print(f"Computer guessed: {cpu_guess}")
    sleep(1)

    #Computer asks for feedback to verify its answer
    feedback = input("Is this number too high(H), low(L), or correct(C)?: ").lower()

    #Computer adjust its new higher number if the guessed is too high
    if feedback == 'h':
        high = cpu_guess - 1

    #Computer adjust its new lower number if the guessed is loo low
    elif feedback == 'l':
        low = cpu_guess + 1

    #Computer guessed the number correctly based on the feedback provided by many tries
    else:
        print("Yes! Computer guessed correctly!\n\n")
        not_guessed = False
