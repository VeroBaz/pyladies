import hangman
import pictures

def test_word():
    word = hangman.get_word()
    assert len(word) >= 6

def test_win_1():
    field = "_ p p l _"
    count = 3
    assert hangman.win(field, count) == "continue"
    assert pictures.get_picture(count) == """+---.
|   |
|
|
|
|
~~~~~~~"""

def test_win_2():
    field = "a p p l e"
    count = 3
    assert hangman.win(field, count) == "win"

def test_win_3():
    field = "_ p p l _"
    count = 9
    assert hangman.win(field, count) == "lose"
    assert pictures.get_picture(count) == """+---.
|   |
|   O
| --|--
|  / \\
|
~~~~~~~"""
