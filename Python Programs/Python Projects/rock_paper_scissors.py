#Python Project #3: Rock, Paper, Sciccors GO!
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from random import choice
from time import sleep

#Declaring the variables
user_choice = ""
cpu_choices = ['r', 'p', 's']
cpu_rand_choice = ""
user_score = 0
cpu_score = 0
game_is_not_over = True

#Program
print("ROCK, PAPER, SCISSORS GO! GAME\n")
sleep(2)

while game_is_not_over:
    user_choice = input("Choose one: rock(r), paper(p) or scissors(s): ").strip().lower()
    cpu_rand_choice = choice(cpu_choices)
    print("ROCK")
    sleep(1)
    print("PAPER")
    sleep(1)
    print("SCISSORS")
    sleep(1)
    print("GO!\n")
    sleep(1)

    if user_choice == 'r' and cpu_rand_choice == 'r':
        print("Draw!\n")
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'p' and cpu_rand_choice == 'p':
        print("Draw!\n")
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")\
        
    elif user_choice == 's' and cpu_rand_choice == 's':
        print("Draw!\n")
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'r'and cpu_rand_choice == 'p':
        cpu_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'r'and cpu_rand_choice == 'p':
        cpu_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'r'and cpu_rand_choice == 's':
        user_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'p'and cpu_rand_choice == 'r':
        user_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 'p'and cpu_rand_choice == 's':
        cpu_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 's'and cpu_rand_choice == 'p':
        user_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    elif user_choice == 's'and cpu_rand_choice == 's':
        cpu_score += 1
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {cpu_rand_choice}\n")
        print(f"User score: {user_score}")
        print(f"Computer score: {cpu_score}\n")

    if user_score == 3:
        game_is_not_over = False
        print("User Wins!\n")

    elif cpu_score == 3:
        game_is_not_over = False
        print("Computer Wins!\n")


