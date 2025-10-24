#!/usr/bin/env python3
''' 
Programmer: Danish Naqvi
Date: 2025-10-24
Course: CIS*1250
Description: Word Frequency Exercise with functions
''' 

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

#function to get and validate the sentence input
def getSentence():
    while True:
        sentence = input("Enter a sentence: ")

        #calling previous function to check if input is a valid sentence
        if is_sentence(sentence):
            return sentence
        else:
            #error trap for if input is not a valid sentence
            print("Please start with a capital letter and end with punctuation (. ! ?)\n")

#function to find the frequency of each word

def calculateFrequencies(sentence):
    words = []          
    frequencies = []    

    #removing punctuation so words like "dog." and "dog" count the same
    cleaned = re.sub(r'[^\w\s]', '', sentence)

    #split the cleaned sentence into individual words
    wordList = cleaned.split()

    #loop through every word in the list
    for word in wordList:
        word = word.lower()  #so its not case sensitive

        #checking if the word already exists in our list
        if word in words:
            index = words.index(word)      #find the position of that word
            frequencies[index] += 1        #and then add 1 to its count
        else:
            #there is a new word so add it to the list with a count of 1
            words.append(word)
            frequencies.append(1)

#returning both lists
    return words, frequencies

#function to print the words and their frequencies
def printFrequencies(words, frequencies):
    print("\nWord frequencies:")

    #print each word with its matching frequency
    for i in range(len(words)):
        
        print(f"{words[i]}: {frequencies[i]}")

    print()  #blank line for a clean output

#main function to connect the previous functions and complete the program
def main():
    print("Welcome to the Word Frequency Counter!")

    sentence = getSentence()                       #get and validate user input
    words, frequencies = calculateFrequencies(sentence)  #calculate frequencies
    printFrequencies(words, frequencies)           #print the results


#starting the program
main()
