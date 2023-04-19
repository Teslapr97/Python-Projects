#Python Project #5: Mad Libs Generator
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from time import sleep
#Declaring Global Variables
noun = ""
noun2 = ""
noun3 = ""
noun4 = ""
verb = ""
verb2 = ""
mad_lib = ""

#Defining the function for generating the Mad Libs
def mad_libs_generetator(name, name2, name3, name4, vrb, vrb2, ):
    mad_libs = f"""
Hey! Welcome to my {name}. 
Here we {vrb} about {name2} and we have fun with {name3}.
Make sure you {vrb2} to my {name4}.\n"""

    return mad_libs

#Program
print("MAD LIBS GENERATOR\n")

noun = input("Enter a noun: ").strip()
noun2 = input("Enter a second noun: ").strip()
noun3 = input("Enter a third noun: ").strip()
noun4 = input("Enter a  fourth noun: ").strip()
verb = input("Enter a verb: ").strip()
verb2 = input("Enter a second verb: ").strip()

mad_lib = mad_libs_generetator(noun, noun2, noun3, noun4, verb, verb2)
print("Generating Mad Libs...\n")
sleep(3)

print(mad_lib)


