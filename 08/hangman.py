import requests
from random import choice
import pictures

def get_word():
    # Generates random word
    url = "https://randomwordgenerator.com/json/words.json"
    word = ""
    while len(word) < 6:
        word = choice(requests.get(url).json()["data"])["word"]
    return word

def get_letter(letters):
    # Gets the player's letter
    check = True
    while check:
        letter = input(f"Guess a letter: ")
        print()
        if not letter.isalpha():
            print("You have to enter a letter.\n")
            continue
        if len(letter) > 1:
            print("You have to enter only one character.\n")
            continue
        if letter in letters:
            print(f"You have already tried letter '{letter}'.\n")
            continue
        check = False
    return letter

def guess(word, field, letters):
    # Puts the player's letter in the field
    letter = get_letter(letters)
    field_list = field.split()
    if letter not in word:
        print(f"No, the letter '{letter}' is not in my word.\n")
        return field, True, letter
    else:
        word_list = [x for x in word]
        count_letter = 0
        for x in word_list:
            if x == letter:
                count_letter += 1
        if count_letter == 1:
            print(f"Yes, there is {count_letter} letter '{letter}'.\n")
            index = get_index(letter, count_letter, word_list)
            field_list[index[0]] = letter
            return " ".join(field_list), False, letter
        else:
            print(f"Yes, there are {count_letter} letters '{letter}'.\n")
            index = get_index(letter, count_letter, word_list)
            while count_letter != 0:
                for x in index:
                    field_list[x] = letter
                    count_letter = count_letter - 1
            return " ".join(field_list), False, letter

def get_index(letter, count_letter, word_list):
    # Gets all the indexes of the letter in the word
    index = []
    enum_word_list = enumerate(word_list)
    for x in enum_word_list:
        if x[1] == letter:
            index.append(x[0])
    return index

def win(field, count):
    # Evaluates whether the game has ended
    field_list = field.split()
    if "_" not in field and count < 9:
        return "win"
    elif count == 9:
        return "lose"
    else:
        return "continue"

def hangman():
    # Launches the game Hangman
    print("I am thinking of a word. What word is it?:\n")
    word = get_word()
    field = len(word) * "_ "
    print(field)
    print()
    count = 0
    letters = []
    while win(field, count) == "continue":
        field, signal, letter = guess(word, field, letters)
        if signal == True:
            count = count + 1
            print(pictures.get_picture(count))
        print(field)
        print()
        letters.append(letter)
        if win(field, count) == "win":
            return "Congratulations, you win!"
        elif win(field, count) == "lose":
            print(f"Sorry, the word was '{word}'.")
            return "Game over!"
