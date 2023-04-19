#Python Project #6: Timer Countdown
#Made by Joshua Ian Carrera Sanchez

#Importing libraries
from time import sleep

#Declaring Global Variables
time = ""

#Defining the function for the timer countdown
def timer_countdown(i):
    for i in range(i, 0, -1):
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)

    print("Time's up!\n")

#User is aksed to enter the countdown in seconds
time = int(input("Enter the time in seconds: "))

#Calling the function
timer_countdown(time)
