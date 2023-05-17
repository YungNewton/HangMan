import time

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("welcome to Hangman")
time.sleep(1.5)
print("Guess the letters in a random word.\nIf your letter is actually a part of the word it is added to the spelling.")
time.sleep(3)
print(f'If not. Hangman is slowly led towards death.')
time.sleep(2)
print(f"If you guess a wrong letter 8 times hangman dies")
time.sleep(2)
print(f' {HANGMANPICS[6]}')
Isplay = input("Enter 'start' if your'e ready to play: ")
