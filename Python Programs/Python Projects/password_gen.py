#Python Project #7: Password Generator
#Made by Joshua I. Carrera-Sanchez

#Importing libraries
from random import choice 
from random import shuffle
from time import sleep

#Declaring Global Variables
letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '+']

#Defining the function for generating a simple password
def password_generator():

    #Declaring local variables
    letter = ""
    number = ""
    symbol = ""
    password = ""
    password_list = []

    #Iterating on each letter on the list randonmly according to the amount of letters
    for i in range(letter_amount):
        letter += choice(letters)
        i += 1

    #Iterating on each number on the list randonmly according to the amount of numbers
    for num in range(number_amount):
        number += choice(numbers)
        num += 1

#Iterating on each symbol on the list randonmly according to the amount of symbols
    for sym in range(symbol_amount):
        symbol += choice(symbols)
        sym += 1

    #Adding the letters, numbers and symbols into one string
    password = letter + number + symbol

    #Converting the string into a new list. Shuffling the list will change the order on the characters
    password_list = list(password)
    shuffle(password_list)

    #Alternate solution to convert the stirng into a list. Shuffling the list will change the order on the characters
    #for char in password:
    #    password_list.append(char)
    #shuffle(password_list)

    #Joining the characters into a single string
    new_password = ''.join(password_list)

    print(f"Your new password is: {new_password}\n")
    
    

#Program
print("PASSWORD GENERATOR\n")
print("Please enter the amount of letters, numbers and symbols to generate a password.\n\n")

letter_amount = int(input("How many letters?: "))
number_amount = int(input("How many numbers?: "))
symbol_amount = int(input("How many symbols?: "))

#Calling the function
print("Generating password...\n\n")
sleep(3)
password_generator()

