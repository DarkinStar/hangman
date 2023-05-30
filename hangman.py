import random


def check(word, guesses):
    uniqueWord = ''.join(set(word))
    uniqueGuesses = ''.join(set(guesses))
    counter = 0
    for l1 in uniqueWord:
        for l2 in uniqueGuesses:
            if l1 == l2:
                counter += 1
    return counter == len(uniqueWord)


# Initializing the game
namesFile = open("russian_nouns.txt", encoding='utf-8')
words = []
for line in namesFile:
    if len(line) < 4:
        continue
    words.append(line.strip())
word = words[random.randint(0, len(words))]
guesses = ''
errores = 0
while errores < 7:
    # print the game progress
    print("Guesses: " + guesses + " word:", end="")

    for letter in word:
        if letter in guesses:
            print(letter, end="")
        else:
            print(".", end="")

    print(" errores:", errores, "/ 7")

    # inputing the guess
    guess = input("Guess: ")
    if len(guess) != 1:
        errores += 1
        continue
    if guess in word:
        guesses = guesses + guess
    else:
        errores += 1
        guesses = guesses + guess

    # check for the end of the game (win/lose)
    if check(word, guesses):
        print(word)
        print("You are a winner!!)")
        break

    if errores == 7:
        print("You lost(, the correct awnser is," + word)
