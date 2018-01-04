

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
    
    if counter == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter + " "
        else:
            result += "_ "
            
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    not_guessed = ""
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            not_guessed += letter

    return not_guessed
            
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    
    guesses = 0
    letters_guessed = []
    previous_letters = []
    
    
    while guesses < 8:
        print("------------")
        print("You have {} guesses left.".format(8 - guesses))
        print("Available letters: {}".format(getAvailableLetters(letters_guessed)))
        
        #gets user's guess
        guess_letter = input("Please guess a letter: ")
        #add letter to list
        letters_guessed += guess_letter
        
        #check the users letter and return responce
        if guess_letter in previous_letters:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letters_guessed)))
        elif guess_letter in secretWord:
            print("Good guess: {}".format(getGuessedWord(secretWord, letters_guessed)))
        else:
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, letters_guessed)))
            guesses += 1
        
        #add letter to list
        previous_letters += guess_letter
        
        #check is word is already guesses
        if isWordGuessed(secretWord, letters_guessed):
            break
    
    print("------------")
    
    #print win or lose based on users guesses
    if isWordGuessed(secretWord, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
    

