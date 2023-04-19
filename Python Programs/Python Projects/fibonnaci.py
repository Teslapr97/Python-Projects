#Python Project #11: Fibonacci Sequence Number Verifier
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from time import sleep

#Defining the function to generate the Fibonacci Sequence:
def fibonacci():

    fibonacci_seq = [0,1]

    for i in range(25):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

        i += 1
        
    return fibonacci_seq

#Defining the function to verify if a number is part of the Fibonacci Sequence:
def verify_number():

    number = int(input("Enter a number: "))

    if number in fibonacci():
        print(f"{number} is part of the Fibonacci Sequence!\n")

    else:
        print(f"{number} is not part of the Fibonacci Sequence!\n")

#Main Program
def main_program():

    print("FIBONACCI NUMBER VERIFIER\n")

    fibonacci()
    verify_number()

#Calling the main_program function
main_program()