#!/usr/bin/env python3
''' 
Programmer: Danish Naqvi
Date: 2025-10-24
Course: CIS*1250
Description: Fibonacci Sequence Exercise with functions
''' 

#function to validate and return user input
def getNum():
    while True:
        try:
#converting input to int
            n = int(input("Enter how many terms you want: "))

#if statement to handle non-positive values
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.\n")

        except ValueError:
#error trap for if the user enters a non-number
            print("Invalid input. Please enter a number.\n")

#function to generate fibonacci sequence
def generateFibonacci(n):
    sequence = []       #stores all the Fibonacci numbers
    first = 0           #first term
    second = 1          #second term

#for loop made to run n amount of times
    for i in range(n):
        sequence.append(first)     #add current number to the list
        nextNum = first + second   #calculate the next term

#update for the next round
        first = second
        second = nextNum

#return the full list when done
    return sequence  

#function to print the sequence and display the numbers
def printSequence(sequence):
    print("Fibonacci sequence:")

#'end=" "' prints on the same line separated by spaces
    for num in sequence:
        print(num, end=" ")

    print("\n")  #\n for clean output

#main function to connect functions and run the program
def main():
    print("Welcome to the Fibonacci Sequence Generator!")

    numTerms = getNum()                    #ask the user for how many numbers
    sequence = generateFibonacci(numTerms) #create the list
    printSequence(sequence)                #show the result

#start the program
main()
