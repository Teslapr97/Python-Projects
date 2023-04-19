#Pyhton Project #1: Guess the Number from CPU
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from random import randint
from time import sleep

#Declaring the variables
random_number = randint(1,100)
user_guess = ""
not_guessed = True

#Program
print("GUESS MY NUMBER GAME!\n\n")
sleep(2)
print("I am thinking of a number between 1 and 100...\n")
sleep(2)

#Ask the user to try a first guess
user_guess = int(input("Which number is it?: "))

#User will be asked again until it guess the number correctly
while not_guessed:
    if user_guess < random_number:
        user_guess = int(input("Higher! Try again: "))

    elif user_guess > random_number:
        user_guess = int(input("Lower! Try again: "))

    elif user_guess == random_number:
        print(f"Yes! {user_guess} is the correct number!\n\n")
        not_guessed = False

