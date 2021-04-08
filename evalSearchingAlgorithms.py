##!/usr/bin/env python
'''
                      ::::::
                    :+:  :+:
                   +:+   +:+
                  +#++:++#++:::::::
                 +#+     +#+     :+:
                #+#      #+#     +:+
               ###       ###+:++#""
                         +#+
                         #+#
                         ###
'''
__author__ = "Alex Pujols"
__copyright__ = "TBD"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"

'''
Title	      :	Evaluating Searching Algorithms
Date		  :	02/02/21
Description   :	A program to evaluate both linear and binary search with intergers/strings
Options	      :	{TBD}
Notes	      :	{TBD}
'''

# Import modules declarations
from random import randint
from collections import Counter
#1from memory_profiler import memory_usage
from time import sleep
import timeit
import string
import random

# Function declarations

# Function to test for valid input and convert to int for further processing
def input_int_validate():
    while True:
        try:
            validate = int(input(": "))
            break
        except:
            print ("Incorrect value! Please make a new selection")
    return validate
# Function to test for valid input and convert to int for further processing
def input_str_validate():
    while True:
        try:
            validate = str(input(": "))
            break
        except:
            print ("Incorrect value! Please make a new selection")
    return validate
# Function to return a random string
def random_string(size):
    temp_string = ' '.join([random.choice(string.ascii_lowercase) for i in range(size)])
    array = temp_string.split()
    return array
# Function to perform linnear search
def linear_search(array, value):
    index = 0
    # Search entire array index starting with 0
    while index < len(array):
        if array[index] == value:
            return True
        index = index + 1
    # If no match is found
    return False
# Function to perfom binary search
def binary_search(array, value):
    # Init lower and upper positions
    lower_index = 0
    upper_index = len(array) - 1
    # Start main loop
    while lower_index <= upper_index:
        # Find mid position
        mid_index = (lower_index + upper_index) // 2
        # Begin Search
        if array[mid_index] == value:
            return True
        else:
            if array[mid_index] < value:
                lower_index = mid_index + 1
            else:
                upper_index = mid_index - 1
    return False
# Main code begins

# Set global vaiables
_samples_ = 10

while True:
    print ("\n")
    print ("Hi, which sort method would you like to run?")
    print ("1 - Linear Search (Integers)")
    print ("2 - Binary Search (Integers)")
    print ("3 - Linear Search (Strings)")
    print ("4 - Binary Search (Strings)")
    print ("0 - EXIT")

    # Take user input and validate
    algorithm = input_int_validate()

    #If user selects linear search for integers
    if (algorithm == 1):
        print ("\nYou selected linear search for integers\n")
        print ("What is the size of the array you wish to create?")
        size = input_int_validate()
        array = [randint(1, 10) for i in range(size)]
        print ("What integer would you like to search for?")
        value = input_int_validate()
        print ("\nARRAY\n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("linear_search(array, value)", setup="from __main__ import linear_search, array, value", number=_samples_)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
        found = linear_search(array, value)
        if found == True:
            print(f"\nThe integer {value} was found!")
        else:
            print(f"\nThe integer {value} was NOT found!")
    # If user selects binary search for integers
    if (algorithm == 2):
        print ("\nYou selected binary search for integers \n")
        print ("What is the size of the array you wish to create?")
        size = input_int_validate()
        array = [randint(1, 10) for i in range(size)]
        # Sort the array in preperation for binary search
        array.sort()
        print ("What integer would you like to search for?")
        value = input_int_validate()
        print ("\nARRAY\n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("binary_search(array, value)", setup="from __main__ import binary_search, array, value", number=_samples_)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
        found = binary_search(array, value)
        if found == True:
            print(f"\nThe integer {value} was found!")
        else:
            print(f"\nThe integer {value} was NOT found!")
    # If user selects linear search for strings
    if (algorithm == 3):
        print ("\nYou selected linear search for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_int_validate()
        array = random_string(size)
        print ("What string would you like to search for?")
        value = input_str_validate()
        print ("\nARRAY\n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("linear_search(array, value)", setup="from __main__ import linear_search, array, value", number=_samples_)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
        found = linear_search(array, value)
        if found == True:
            print(f"\nThe string {value} was found!")
        else:
            print(f"\nThe string {value} was NOT found!")
    # If user selects binary search for strings
    if (algorithm == 4):
        print ("\nYou selected binary search for strings \n")
        print ("What is the size of the array you wish to create?")
        size = input_int_validate()
        array = random_string(size)
        # Sort the array in preperation for binary search
        array.sort()
        print ("What string would you like to search for?")
        value = input_str_validate()
        print ("\nARRAY\n", array)
        # To time the execution of the algorithm for analysis
        times = timeit.repeat("binary_search(array, value)", setup="from __main__ import binary_search, array, value", number=_samples_)
        print (f"\nThe minimum time to execute across {_samples_} samples was: {format(min(times), '.10f')} seconds!")
        found = binary_search(array, value)
        if found == True:
            print(f"\nThe string {value} was found!")
        else:
            print(f"\nThe string {value} was NOT found!")
    #If user selects exit
    if (algorithm == 0):
        print ("\n You have chosen to leave the program.  Goodbye! \n")
        break
