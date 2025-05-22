#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 22, 2025
# This program generates and displays ten
# random numbers from 0 to 100 with lists
# and then displays the maximum number.

# Import the constants module for useful constants.
import constants

# Import the random module for the random integer function.
import random


# Define a function to get the maximum
# number out of a number list.
def find_max_value(num_list):
    # Initialize the current maximum
    # number to zero to use it later.
    current_max_value = 0

    # Use a for loop to loop over the length of the list.
    for index in range(len(num_list)):
        # Check if the indexed number is greater
        # than the current maximum number.
        if num_list[index] > current_max_value:
            # Set the current maximum value
            # to the indexed number.
            current_max_value = num_list[index]

    # Return the resulting maximum value.
    return current_max_value


# Define the main function.
def main():
    # Print an empty space to format text.
    print("")
    # Initialize a list of integers as
    # an empty list to be used later.
    list_of_int = []

    # Use a for loop to loop over the maximum array
    # size to generate the ten random numbers.
    for index in range(constants.MAX_ARRAY_SIZE):
        # Generate a random number from the minimum number
        # size, 0, to the maximum number size, 100.
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Populate the list by appending the random number.
        list_of_int.append(random_number)

        # Display information about the random
        # number and its current position.
        print(f"{random_number} added to the list at position {index}.")

    # Determine the maximum number by assigning
    # it to the maximum value function.
    max_number = find_max_value(list_of_int)
    # Display the maximum number.
    print(f"\nThe max value is: {max_number}.\n")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
