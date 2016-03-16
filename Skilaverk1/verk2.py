#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random as r

def main():
    print('>>>Nýr leikur<<< \n')
    svar = generateAnswer()
    while True:
        userGuess = getUserGuess()
        if userGuess == svar:
            print("Til hamingju þú vannst")
            return
        print('Því miður er svarið vitlaust, vonandi mun þetta hjálpa þér')
        giveFeedback(svar,userGuess)

def generateAnswer():
    tolur = [str(x) for x in range(8)]
    svar = ''
    for i in range(5):
        tala = r.sample(tolur, 1)[0]
        tolur.remove(tala)
        svar += tala
    return svar

def getUserGuess():
    numberOfGuesses = 0
    while numberOfGuesses < 8:
        userGuess = raw_input('Giskaðu á 5 stafa tölu')
        if len(userGuess) != 5:
            continue
        guessIsValid = True
        for x in userGuess:
            if userGuess.count(x) != 1 or ord(x) not in range(48,58):
                guessIsValid = False
                break
        if guessIsValid:
            return userGuess
    numberOfGuesses + 1
    if numberOfGuesses == 8:
        raw_input('Sorry, you\'ve lost the game, would you like to try again?(Y/N)')
        main()

def giveFeedback(svar, userGuess):
    for i in range(5):
        if userGuess[i] == svar[i]:
            print 'X',
            continue
        print('-'),
    print '\n'

main()
