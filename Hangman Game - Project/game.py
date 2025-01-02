

'''
The Hangman game asks the user for a valid username and then randomly selects a country name. The user guesses letters, with the game displaying blanks for unguessed letters. It tracks correct and incorrect guesses, showing feedback on remaining chances. The game ends when the user guesses the word correctly or runs out of attempts (6 wrong guesses)
'''


from words import word_list as wl, alphabets as al #imported list of words
import random as r
word=r.choice(wl) #using python built in library "random" function "choice" to generate a random word from the word list we provide.
word=word.lower()

def hangman(word, al):
    while True:
        try:
            username=input("Hello, Welcome to Muniv2 hangman. Please enter your username and make sure it only contains alphabets: ")
            if username.isalpha():
                print(f"Nice to meet you {username}, lets start!", end="\n")
                print("Hint: The word is a countrys' name", end="\n")
                break
            else:
                raise TypeError
        except TypeError:
            print("Invalid username, try again.", end="\n")

    #greetings done to user

    tempword=set(i for i in word if i.isalpha()) #contains unguessed letters
    ag=set() #contains already guessed letters
    for i in word:
        if i.isalpha():
            print("_", end="")
        else:
            print(i, end="")
    print()

    #word displayed in terms of blanks

    count=0
    flag=1
    while flag==1:
        try:
            print("Unguessed letters till yet: ", end="\n")
            for i in al:
                if i not in ag:
                    print(i, end=", ")
            print()

            #prints unguessed letters after each guess

            letter=input("Enter a letter that you think is present in this word: ")
            if len(letter)==1 and letter.isalpha():
                if letter in tempword:
                    ag.add(letter)
                    print(f"Good guess, {letter} is present in the countrys' name", end="\n")
                    tempword.remove(letter)

                #if correct guess

                elif (letter in word) and (letter not in tempword):
                    print(f"You have already guessed {letter}, try guessing a different letter", end="\n")

                #if already guessed

                else:
                    print(f"Oops, wrong guess. {letter} is not present in the countrys' name", end="\n")
                    ag.add(letter)
                    count+=1
                    if count!=6:
                        print(f"You have {6-count} chances left", end="\n")

                    #if wrong guess

                if count==6 or tempword==set():
                    flag=0
                    break
                for z in word:
                    if (z.isalpha()) and (z in tempword):
                        print("_", end="")
                    else:
                        print(z, end="")
                print()

                #updated word displayed in terms of blanks
                
            else:
                print("Invalid input, try again", end="\n")
        except ValueError and IndexError and TypeError:
            print("Invalid input, try again", end="\n")

    if tempword==set():
        print(f"Congrats you guessed the word correctly, the word was: {word}", end="\n")

    #condition if user win

    elif count==6:
        print(f"Damn, you couldn't guess the word correctly, the word was: {word}", end="\n")

        #condition if user lost
        
hangman(word, al)
                
            


