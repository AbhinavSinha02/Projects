#this code aims at speeding up the process of carrying out easy but lengthy calculations.
#this code will be able to carry out calculations such as parameters of a square/rectangle/circle
#solutions of quadratic equations, GCD computation using euclid's algorithm, calculationg sum of all numbers, multiplication of all numebrs,
#mean of numbers, greates of all number out of the given numbers, filtering positive or negative numbers from a given set.
#code contains a total of 11 functions.

import math
def parameters_of_square(size_of_side):
    perimeter=  size_of_side*4
    area= size_of_side*size_of_side
    diagonal= (math.sqrt(2))**size_of_side
    print(f"perimeter of square",perimeter)
    print(f"area of square", area)
    print(f"diagonal of square", diagonal)
    return

def parameter_of_rectangle(length,breadth):
    perimeter = length*breadth*2
    area = length*breadth
    diagonal = math.sqrt((length*length)+(breadth*breadth))
    print(f"perimeter of rectangle", perimeter)
    print(f"area of rectangle", area)
    print(f"diagonal of rectangle", diagonal)
    return

def parameter_of_circle(radius):
    area=math.pi*radius*radius
    circumference=2*math.pi*radius
    return

def solution_of_quadratic_equation(a,b,c):
    #this is yet to be completed.