'''
Created on Oct 16, 2016

@author: Prathmesh Patel
'''

import random

def fileToStringList(filename):
    #opens file and returns a list of strings(words)
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    
     
def getPossibleWords(wordlist,length):
    # returns a list of words from wordlist having a specified length 
    return[word for word in wordlist if len(word)==length]


def displayGuess(wordList):
    #list of characters with letters correctly guessed and '_' for letters not quessed yet: returns the list as a String
    return ' '.join(wordList)

def guessStart(word):
    #returns a list of single characters '_' the same size as the wordToGuess
    return ['_']*len(word)

def miss(guessList,wordToGuess, letter):  
    # helper function to use as an update for a counter for number of user misses
    misses = 0
    if letter in wordToGuess:
        misses += 0
    else:
        misses +=1
    return misses

def updateLetter(guessList,wordToGuess, letter):
    # updates _ to the letter guessed if guessed correctly and then prints if this happens. If this doesn't happen, it prints as a miss, return updated guessList
    for x in range(len(wordToGuess)):
        if wordToGuess[x]==letter:
            guessList[x]= letter
    if letter in wordToGuess:
        print "You guessed a letter!"
        
    else:
        print "That's a MISS"    
    return guessList   

def playGame(words):
    #setup for game, uses raw_inputs 
    guessLength = int(raw_input("how many letters in word to guess? "))     #how many letters in the word you want to guess
    numberMisses = int(raw_input("how many misses allowed? "))  #how many misses can you allow in the game
    wordsOfLength = getPossibleWords(words,guessLength)    # creates list of all possible words with length inputted
    wordToGuess = random.choice(wordsOfLength)              # random choice from above list
    guessList = guessStart(wordToGuess)         # creates guessList as underscores for every letter in word

    count = 0 #counter for number of guesses
    misses = 0 #counter for number of misses
    strAlphabet = "abcdefghijklmnopqrstuvwxyz"  #will remove letters as they are guessed
    while True:
        if guessList.count('_') == 0: # all letters guessed
            break
        print "guessed so far:", displayGuess(guessList)
        letter = raw_input("guess a letter: ") #guess 
        if letter == "+": #guess the word if inputted
            guess = raw_input("guess the word:")
            if guess == wordToGuess:
                print "THAT'S RIGHT! YOU WIN!"
                break #game ends
            else:
                print "That's wrong. BUMMER. You lose. The word was:", wordToGuess
                break #game ends
        updateLetter(guessList, wordToGuess, letter) #updates guesslist
        strAlphabet = strAlphabet.replace(letter,"") #removes guessed letter from string of alphabet
        print "letters not guessed:", strAlphabet
        count +=1 #count +1 for number of guesses
        misses += miss (guessList, wordToGuess, letter) #updates number of misses
        if misses == numberMisses: #number of misses used up
            break #game ends
        print numberMisses - misses, "misses left" #total misses inputted minus how many you missed
        print "guess a letter or enter + to guess the word"

        
    # prints game over based on spaces cleared or misses used up
    if guessList.count('_') == 0 and misses < numberMisses:
        print "You win. You guessed the word", wordToGuess
        print "You guessed", count," times"
    elif misses == numberMisses:
        print "You lost, word was", wordToGuess
        print "You guessed incorrectly", misses, "times, smh"

if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    playGame(words)
