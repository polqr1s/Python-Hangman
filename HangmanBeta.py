#Hangman from scratch
#Beta build
#Pictures of the man hanging will be added
#Difficulty levels will be added

import random

words = ["notice", "crabby", "rightful", "ink", "collect", "violet", "scatter"]
#Using preset words for now until I find out how to use the dictionary library

def menu():
    print("\nWelcome!")
    while True:
        print("\nMain Menu")
        print("Enter 'start' to start")
        user_input = input(": ")
        if user_input == "start" or user_input == "Start":
            wordpick()
        else:
            print("Invalid Entry!")
    

def wordpick():
    tries = 10
    ranWord = random.randint(0, 6)
    wordAsList = list(words[ranWord])
    #print (''.join(wordAsList))
        #Printing for bugtesting
    blanks = list("_" * (len(wordAsList)))
    x = 0
    
    while True:
        print("\nNumber of letters in the random word:")
        print(len(words[ranWord]))
        print (' '.join(blanks))
        
        if "_" not in blanks:
            print("##### Winner! #####")
            menu()
            
        print("Guess a letter you think is in the word!")
        print("Tries left: ", tries)
        user_input = input(": ")
        
        if str(user_input) == "quit":
            menu()
        if (len(user_input)) >= 2:
            print("Guess only ONE Letter!")
        elif user_input == "":
            print("You can't enter nothing!")
        elif str(user_input) not in str(words[ranWord]):
            print("\nIts not in there!")
            tries = tries - 1
            if tries <= 0:
                print("\nGame over!")
                print("The word was:", words[ranWord])
                menu()
        elif str(user_input) in str(words[ranWord]):
            print("\nIts in there!")
            for letter in enumerate(words[ranWord]):
                #print(letter)
                    #Printing for bugtesting
                if user_input in letter:
                    #print(letter[1])
                        #Printing for bugtesting
                    x = letter[0]
                    blanks[x] = letter[1]

menu()
