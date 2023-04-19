#Python Project #4: Ohm's Law Calculator
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from time import sleep

#Declaring Global Variables
choice = ""
ohms = ""
amps = ""
volts = ""


#Defining the function for calculating the resistance
def resistance(x, y):
    result = round(x / y, 2)
    return result

#Defining the function for calculating the current
def current(num1, num2):
    total = round(num1 / num2, 3)
    return total

#Defining the fucntion for calculating the voltage\
def voltage(val1, val2):
    product = round(val1 * val2, 2)
    return product

#Program
print("OHM'S LAW CALCULATOR\n")
while choice != 'none':

    choice = input("What would you like to calculate (v/r/i/none)?: ").lower().strip()

    if choice == 'r':
        volts = float(input("Enter the volatge value: "))
        amps = float(input("Enter the current value: "))
        ohms = resistance(volts, amps)
        print(f"Resistance value: {ohms} kΩ\n")

    elif choice == 'i':
        volts = float(input("Enter the volatge value: "))
        ohms = float(input("Enter the resistance value: "))
        amps = current(volts, ohms)
        print(f"Current value: {amps} mA\n")

    elif choice == 'v':
        amps = float(input("Enter the current value: "))
        ohms = float(input("Enther the resistance value: "))
        volts = voltage(amps, ohms)
        print(f"Voltage value: {volts} V\n")

    