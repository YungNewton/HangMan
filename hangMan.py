import time
import random

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
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
final = []
print("welcome to Hangman")
time.sleep(1.5)
print("Guess the letters in a random word.\nIf your letter is actually a part of the word it is added to the spelling.")
time.sleep(3)
print(f'If not. Hangman is slowly led towards death.')
time.sleep(2)
print(f"If you guess a wrong letter 8 times hangman dies")
time.sleep(2)
print(f' {HANGMANPICS[6]}')
isplay = input("Enter 'start' if you're ready to play: ")
isSure = 'N'
if isplay.lower() == "start":
    print("GAME ON!!!")
else:
    isSure = input("Enter the word 'start' if your'e willing to play\nIf not enter 'N' for no: ")
if isplay.lower == "start" or isSure.lower != 'n':
    games = int(input("how many games do you want to play?: "))
    for i in range(games):
        word = random.choice(words)
        length =  len(word)
        print(f'Your word is a {length} letter word')
        print('')
        for d in range(length):
            print('__ ',end ="")
            final.append("__")
        print("")
        print("")
        for a in range(8):
            position = 0
            print(word)
            UserChoice = input('Guess a letter: ')
            if UserChoice in word:
                print(f'CORRECT! {UserChoice} is actually a part of the word.')
                print("")
                for s in range(length):
                    if word[position] == UserChoice:
                        final[position] = UserChoice.upper()
                    position+=1
                print(*final)
                print('')
            else:
                print

else:
    print("Rerun Code Whenever you want to start and Enter start on Prompt")                


