"""
Name: Bria Weisblat
Date: 08/28/24
Assignment: Assignment #1
Due Date: 09/04/24
About this project: This program takes a user-inputted integer and displays the smallest prime triplet whose
smallest prime is no less than the number entered.
Assumptions: Assumes integer user input and considers prime triplets in the forms (p, p+2, p+6) and (p, p+4, p+6)
Extra Credit: The execution time of this program for the number 1,000,000,000,000 is 9.08 seconds
All work below was performed solely by Bria Weisblat
"""

import math

def isprime(n):
    # Check if divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check up to the square root of n
    limit = int(math.isqrt(n)) + 1
    # Use 6k optimization (all prime numbers greater than 3 are in the form 6k +1 or 6k-1)
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def nextprime(n):
    candidate = n + 1
    # If even (not prime), make it odd (potential prime)
    if candidate % 2 == 0:
        candidate += 1
    # Continue checking until a prime is found
    while not isprime(candidate):
        candidate += 2  # Skip even numbers
    return candidate

# Prompt the user to enter an integer
userInput = int(input("Enter a number: "))

# Store the original input
originalInput = userInput

# All inputs <=5 should output the smallest possible prime triplet
if userInput <= 5:
    print("(5, 7, 11)")
else:
    # If the user input is NOT prime
    if not isprime(userInput):
        # Find the smallest prime number larger than the user input
        userInput = nextprime(userInput)
    firstNum = userInput
    secondNum = 0
    thirdNum = 0
    isTriplet = False
    # While a triplet has not been found
    while not isTriplet:
        # Check to see if the first prime + 6 is also prime
        thirdNum = firstNum + 6
        # If the first prime + 6 is prime
        if isprime(thirdNum):
            # The second number in the triplet can be in the form p + 2 or p + 4
            # Check to see if p + 2 is prime
            if isprime(firstNum + 2):
                isTriplet = True
                secondNum = firstNum + 2
                # Print the triplet when found
                print(f"The smallest triplet larger than {originalInput} is ({firstNum}, {secondNum}, {thirdNum})")
            # Check to see if p + 4 is prime
            elif isprime(firstNum + 4):
                isTriplet = True
                secondNum = firstNum + 4
                # Print the triplet when found
                print(f"The smallest triplet larger than {originalInput} is ({firstNum}, {secondNum}, {thirdNum})")
        # If a triplet is not found, find a new first prime
        firstNum = nextprime(firstNum)