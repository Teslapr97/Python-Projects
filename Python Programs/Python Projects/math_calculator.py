#Python Project # 8: Math Calculator
#Made by Joshua Ian Carrera-Sanchez

#Importing libraries
from time import sleep
from math import sqrt
import cmath
from os import system

#Declaring Global Variables



#Defining the function for Pyhtagorean Theorem Solver
def pythagorean_theorem():
    side_a = ""
    side_b =""
    hypotenuse = ""

    print("PYTHAGOREAN THEOREM\n")
    print("Choose one of the following:\n")
    print("1. Calculate side a.")
    print("2. Calculate side b.")
    print("3. Calculate hypotenuse.\n")
    choice = int(input("Select a number from 1-3: "))

    if choice == 1:

        system('cls')
        side_b = float(input("Side of b: "))
        hypotenuse = float(input("Side of hypotenuse: "))
        side_a = sqrt(pow(hypotenuse, 2) - pow(side_b, 2))
        print(f"Side a: {side_a}\n")

    elif choice == 2:

        system('cls')
        side_a = float(input("Side of a: "))
        hypotenuse = float(input("Side of hypotenuse: "))
        side_b = sqrt(pow(hypotenuse, 2) - pow(side_a, 2))
        print(f"Side a: {side_b}\n")

    elif choice == 3:

        system('cls')
        side_a = float(input("Side of a: "))
        side_b = float(input("Side of b: "))
        hypotenuse = sqrt(pow(side_a, 2) + pow(side_b, 2))
        print(f"Side a: {hypotenuse}\n")

#Defining the function for Trigonometric Functions Solver
def trigonometric_functions():

    sin = ""
    csc = ""
    cos = ""
    sec = ""
    tan = ""
    cot = ""
    op = ""
    adj = ""
    hyp = ""

    system('cls')
    print("TRIGONOMETRIC FUNCTIONS\n")
    print("Choose one of the following:\n")
    print("1. Calculate the sine/cosecant.")
    print("2. Calculate cosine/secant.")
    print("3. Calculate tangent/cotangent.\n")
    choice = int(input("Select a number from 1-3: "))

    if choice == 1:

        system('cls')
        op = float(input("Opposite side: "))
        hyp = float(input("Hypotenuse side: "))
        sin = round(op / hyp, 3)
        csc = round(1 / sin, 3)
        print(f"Sine: {sin}")
        print(f"Cosecant: {csc}")

    elif choice == 2:

        system('cls')
        adj = float(input("Adjacent side: "))
        hyp = float(input("Hypotenuse side: "))
        cos = round(adj / hyp, 3)
        sec = round(1 / cos, 3)
        print(f"Cosine: {cos}")
        print(f"Secant: {sec}")

    elif choice == 3:

        system('cls')
        op = float(input("Opposite side: "))
        adj = float(input("Adjacent side: "))
        tan = round(op / adj, 3)
        cot = round(1 / tan, 3)
        print(f"Tangent: {tan}")
        print(f"Cotangent: {cot}")

#Defining the function for Quadratic Equation Solver

def qudratic_equation_solver():

    system('cls')
    print("QUDRATIC EQUATION SOLVER\n")
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = pow(b, 2) - (4 * a * c)

    if discriminant == 0:

        print("Equation has only one real solution.\n")
        x1 = (-b + discriminant) / (2 * a)
        x2 = (-b - discriminant) / (2 * a)

        print(f"Solutions: x1 = {x1}, x2 = {x2}\n")

    elif discriminant > 0:

        print("Equation has two real solutions.\n")
        x1 = (-b + discriminant) / (2 * a)
        x2 = (-b - discriminant) / (2 * a)
        print(f"Solutions: x1 = {x1}, x2 = {x2}\n")

    elif discriminant < 0:

        neg_discriminant = cmath.sqrt(pow(b, 2) - (4 * a * c))

        print("Equation has two imaginary complex solutions.\n")
        x1 = (-b + neg_discriminant) / (2 * a)
        x2 = (-b - neg_discriminant) / (2 * a)
        print(f"Solutions: x1 = {x1}, x2 = {x2}\n")

#Defining the function for Geometry Solver
def geometry_solver():
    print("GEOMETRY SOLVER\n")

    print("Choose one of the following:\n")
    print("1. Calculate the perimeter/area of a square.")
    print("2. Calculate the periemter/area of a rectangle.")
    print("3. Calculate the perimeter/area of a triangle.\n")
    print("4. Calculate the circunference/area of a circle.")
    choice = int(input("Select a number from 1-4: "))

    if choice == 1:

        system('cls')
        l_square = float(input("Enter the lenght: "))
        square_perim = 4 * l_square
        square_area = pow(l_square, 2)

        print(f"Perimeter: {square_perim}")
        print(f"Area: {square_area}")

    elif choice == 2:

        system('cls')
        l_rectangle = float(input("Enter the lenght: "))
        w_rectangle = float(input("Enter the width: "))
        rectangle_perim = 2 * (l_rectangle + w_rectangle)
        rectangle_area = l_rectangle * w_rectangle

        print(f"Perimeter: {rectangle_perim}")
        print(f"Area: {rectangle_area}")

    elif choice == 3:

        system('cls')
        b_triangle = float(input("Enter the base: "))
        h_triangle = float(input("Enter the height: "))
        hyp_traingle = float(input("Enter the hypotenuse: "))
        triangle_perim = b_triangle + h_triangle + hyp_traingle
        triangle_area = 0.5 * b_triangle * h_triangle

        print(f"Perimeter: {triangle_perim}")
        print(f"Area: {triangle_area}")

    elif choice == 4:

        system('cls')
        r_circle = float(input("Enter the radius: "))
        circle_circun = 2 * r_circle * 3.14
        circle_area = 3.14 * pow(r_circle, 2)

        print(f"Circunference: {circle_circun}")
        print(f"Area: {circle_area}")



#Program
print("MATH CALCULATOR\n")
print("Select on the following:")

print("1. Pythagorean Theorem.")
print("2. Trigonometric Functions Solver.")
print("3. Quadratic Equation Solver.")
print("4. Geometry Solver\n")

math_choice = int(input("Select a number from 1-4: "))

if math_choice == 1:
    system('cls')
    pythagorean_theorem()

elif math_choice == 2:
    system('cls')
    trigonometric_functions()

elif math_choice == 3:
    system('cls')
    qudratic_equation_solver()

elif math_choice == 4:
    system('cls')
    geometry_solver()

