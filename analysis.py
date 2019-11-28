# File: analysis.py
# Author: Tony Gaddis and ziad sakr
# Lab section: Wednesday and Thursday
#
# Created:  01/01/18
# Modified: 02/25/18
#

import random

# main function
def main():

    #Local variables
    nums = [] #empty list
    
    # Generates a file called "random_numbers.txt" with random 20 values ranging from 1 to 10
    # Add your code here


    # Reads in numbers from "random_numbers.txt" and saves them in a list called rnd_numbers
    nums = read_numbers_file("expenses")

    # Prints out the nums list for testing. It should contain numbers
    # read in from "random_numbers.txt" 
    for i in nums:
        print(i, end=" ")

    # Analyzes values in the nums list and saves the output to "analysis.txt"
    print()
    analyze_numbers(nums, "analysis")


# This function generates a text file with random numbers as specified by the user
def generate_numbers_file(file_name, total_numbers, lower_end, upper_end):
    number = 0
    file_name = file_name + ".txt"

    outfile = open(file_name, 'w')
    for i in range(total_numbers):
        number = random.randint(lower_end, upper_end)
        outfile.write(str(number) + '\n')

    outfile.close()
    print('Data written to ' + file_name + '.')

# This function reads in values from a file, adds them to a list and returns the list
def read_numbers_file(file_name):
    file_name = file_name + ".txt"
    infile = open(file_name, 'r')

    # Add your code here to create an empty list and to add each line from infile
    # to the list using the append() method. Note that you need to convert
    # each line to int first.


    infile.close()

    print('Data read from ' + file_name + '.')
    return numbers_list

# This function takes a name of a list and a name of a file as arguments to
# analyze numbers in the list and write the results to a file.
def analyze_numbers(num_list, file_name):
    # Add your code here to calculate length, max, min, total and average
    # of all elements in the num_list




    
    file_name = file_name + ".txt"    
    outfile = open(file_name, 'w')

    # Add your code here to write the results to outfile.
    # See the expected output in the handout.



    


    outfile.close()
    print('Data written to ' + file_name + '.')

main()
