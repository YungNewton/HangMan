import time
import random

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
    '''
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
death = 0
isWin = False
isHung = False
score = 0
print("welcome to Hangman")
time.sleep(1.5)
print("Guess the letters in a random word.\nIf your letter is actually a part of the word it is added to the spelling.")
time.sleep(3)
print(f'If not. Hangman is slowly led towards death.')
time.sleep(2)
print(f"If you guess a wrong letter 8 times hangman is hung")
time.sleep(2)
print(f' {HANGMANPICS[7]}')
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
        for d in range(length):
            final.append("__")
        while isHung == False and isWin == False:
            if "__" in final:
                print("",end="")
            else:
                print("HURRAY!!!")
                time.sleep(0.5)
                print("You Got the Word")
                time.sleep(1)
                print("")
                print(*final)
                print("")
                score+=1
                print(f"score : {score} out of {games} games.")
                isWin == True
                break
            if isWin == False:
                position = 0
                #print(word)
                print("")
                print(*final)
                print("")
                print("")
                UserChoice = input('Guess a letter: ')
                if UserChoice.lower() in word:
                    print(f'CORRECT! {UserChoice} is actually a part of the word.')
                    for s in range(length):
                        if word[position] == UserChoice:
                            final[position] = UserChoice.upper()
                        position+=1
                else:
                    print("")
                    print(*final)
                    print("")
                    print(f"Opps!! {UserChoice} is not a letter in this word.")
                    time.sleep(1)
                    print("Try again.")
                    time.sleep(0.5)
                    if death == 0:
                        print("")
                        print("Hang mans gallow has been made.")
                        print(f"{HANGMANPICS[death]}")
                        time.sleep(1)
                        print("Hang man Still trusts you though. Don't let him Die")
                        time.sleep(2)
                    elif death ==1:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print(HANGMANPICS[death])
                    elif death ==2:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print(HANGMANPICS[death])
                    elif death ==3:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print("Hang Man says he will be hung if you fail four more times")
                        time.sleep(1.5)
                        print(HANGMANPICS[death])
                    elif death ==4:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print("Hang Man says he will be hung if you fail three more times")
                        time.sleep(1.5)
                        print(HANGMANPICS[death])
                    elif death ==5:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print("Hang Man is now scared")
                        time.sleep(1.5)
                        print(HANGMANPICS[death])
                    elif death ==6:
                        print("")
                        print("hang Man's hanging is proceeding.")
                        time.sleep(1)
                        print("Hang Man says he will be hung if you fail 1 more times")
                        time.sleep(1.5)
                        print(HANGMANPICS[death])
                    elif death ==7:
                        print("")
                        print("hang Man has been hung!")
                        time.sleep(1.5)
                        print(HANGMANPICS[death])
                        time.sleep(1)
                        print("Try again")
                        print(f"Your Word Was {word.upper()}")
                        isWin = True
                    death+=1

else:
    print("Rerun Code Whenever you want to start and Enter start on Prompt")                


