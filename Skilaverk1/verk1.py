#Start by importing random
import random

#The number that the computer randomly generates
tolvutala = random.randint(1,99)

#User's points, always 0 at start
stig = 1280

#User's tries to guess the correct number
tilraunir = 0

#User's guess
gisk = int(input("Guess a number"))

#Keyra while-loop á meðan að tilraunir eru færri en 8
while tilraunir < 8:
    #bæta við tilraun í hvert skipti sem loopan keyrir
    tilraunir = tilraunir +1
    if gisk > tolvutala:
        print("Your number is too big!")
        gisk = input("Try again")
    elif gisk < tolvutala:
        print("Your number is too small!")
        gisk = input("Try again")
    #þessi elif checkar hvort að gisk hafi verið rétt, endar svo while-loop
    elif gisk == tolvutala:
        break
    #Deila stig með 2 fyrir hverja tilraun.
    stig = stig / 2

#If loopa checkar hvort giskað hafi verið rétt
if gisk == tolvutala:
    print("Congratz!")
    print("You guessed on your " + str(tilraunir)  + " try! That means you get " + str(stig) + " points!")
else:
    print("Sorry you've used up all of your guesses!")
    print("The number was: " + str(tolvutala))
