import random

#variables
looping = True
newLine = "------------------------------------------"
guessing = True

class Game():
    def __init__(self):
        f = open("words.txt").read().splitlines()
        word = random.choice(f)

        self.originalWord = word
        self.showedWord = word
        self.word = word
        self.guesses = 10

        print(newLine)
        print("\nTHE GAME HAS STARTED!\n")
        print(newLine)

        self.guess()




    def guess(self):
        while guessing:
            #Checks amount of guesses
            if self.guesses == 0:
                print(newLine)
                print("\nOUT OF GUESSES! ")
                print("The word was: " + self.originalWord + "\n")
                print(newLine)
                break

            #Starts taking input
            ans = input("Take a guess: ")
            #Checks
            if ans in self.word:
                x = self.removeC(ans)

                if x == "done":
                    break

                wLen = self.length()

                print("There is now " + str(wLen) + " letters left! ")

            else:
                #If wrong, take away a guess
                self.guesses -= 1
                print("WRONG! You now have " + str(self.guesses) + " guess(es) left!")




    def removeC(self, c):
        self.word = self.word.replace(c, "")

        if self.length() == None:
            print(newLine)
            print("\nYou have won! Congratulations!\n ")
            print(newLine)
            return "done"




    def length(self):
        if self.word:
            return len(self.word)

    def editShowed(self, c):
        pass

#TODO When guessed right, take the index of where it's right and put it in the self.showedWord & replace the other letters with _    //// take the length of self.word & take the index of where it's right then replace that index of the showed word with the letter they guessed right     

        



game1 = Game()