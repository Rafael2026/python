import sys

from datetime import date

sum = 1 + 2 #3
product = sum * 2
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # looks like a float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
left_side = 10
right_side = 5

parsecs = 11
lightyears = parsecs * 3.26

left_side / right_side # 2
date.today()

name = input("Enter your name: ")
first_number = input("First number: ")
second_number = input("Second number: ")
parsecs_input = input("Input number of parsecs:")


print(sum)
print(product)
print("show this in the console")

# print["show this in the console"]

type(distance_to_alpha_centauri) ## <class 'float'>

print(date.today())

# print("Today's date is: " + date.today())

print("Today's date is: " + str(date.today()))

print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

print(sys.argv)

print(sys.argv[0]) # program name

print(sys.argv[1]) # first arg

print("Welcome to the greeter program")


print("Greetings " + name)

print("calculator program")

print(first_number + second_number)
print(int(first_number) + int(second_number))

parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

# print("1" + 2)