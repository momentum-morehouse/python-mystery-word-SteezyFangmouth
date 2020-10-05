from random import randint
file_reader = open("words.txt", "r")

#Number of Lines Per Letter
def getLines():
    
    num_lines = sum(1 for line in open('words.txt'))
    return num_lines

def gameInfo(number_of_lines):
    #Game Name
    print("Guess The Word!")

    #Number of Words
    print("There are", getLines(), "words.")

#Random Word
def random_Word(number_of_lines):
    index = randint(0, number_of_lines)
    words = file_reader.readlines()
    word = words[index]
    wordLength = len(word)

#Word Lenght Is Equal To Unknown Word
def createEmptyWord(word):
    guessProgress = ""
    while (len(guessProgress) < ((len(word)-1)*2)):
        guessProgress += "_ "
    
    print ("Length of word: ", (len(word)-1))
    print ("Length of guessProgress: ", (len(guessProgress)))
    print (guessProgress)
    return guessProgress

#Word Guess Matches Unknown Word
def matchCheck(guess):
    index = 0
    for letter in word:
        if(guess == letter):
            string_list = list(emptyWord)
            string_list[index] = guess
            emptyWord = "".join(string_list)
        index += 2
    print (emptyWord)
    return emptyWord        
   
def guessPrompt(attempts):

    newEmptyWord = emptyWord
    status = False

    while(attempts > 0):
        print("", attempts, " Tries Left")
        guess = input("Enter a letter: ")
    
        if(len(guess) > 1):
            print("Invalid")
            playerGuesses(word, newEmptyWord)
        else:
            newEmptyWord = matchCheck(newEmptyWord, guess, word)
            attempts -= 1
            guessPrompt(attempts,word,newEmptyWord)

        for letter in newEmptyWord:
            if(letter == "_"):
                status = False
            else:
                status = True
    return status

def gameStatus(status):
    playerStatus = ""
    if(status == True):
        playerStatus = "Correct!"
    else:
        playerStatus = "Sorry, you're wrong. Try again"

    return playerStatus