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
random_words =('able about account acid across act addition adjustment advertisement after again against agreement '
              'air all almost among amount amusement and angle angry animal answer ant any apparatus apple approval '
              'arch argument arm army art as at attack attempt attention attraction authority automatic awake '
              'baby back bad bag balance ball band basebasin basket bath be beautiful because bed bee before behaviour '
              'belief bell bent berry between bird birth bit bite bitter black blade blood blow blue board boat body '
              'boiling bone book boot bottle box boy brain brake branch brass bread breath brick bridge bright broken '
              'brother brown brush bucket building bulb burn burst business but butter button by '
              'cake camera canva card care carriage cart cat cause certain chain chalk chance change cheap cheese chemical '
              'chest chief chin church circle clean clear clock cloth cloud coal coat cold collar colour comb come comfort '
              'committee common company comparison competition complete complex condition connection conscious control cook '
              'copper copy cord cork cotton cough country cover cow crack credit crime cruel crush cry cup cup current curtain '
              'curve cushion damage danger dark daughter day  dead dear death debt decision deep degree delicate dependent '
              'design desire destruction detail development different digestion direction dirty discovery discussion disease '
              'disgust distance distribution division do dog door doubt down drain drawer dress drink driving drop dry dust '
              'ear early earth east edge education effect egg elastic electric end engine enough equal error even event ever '
              'every example exchange existence expansion experience  expert eye face fact fall false family far farm fat '
              'father fear feather feeble feeling female fertile fiction field fight finger fire first  fish fixed flag '
              'flame flat flight floor flower fly fold food foolish foot for force fork form forward fowl frame free  frequent '
              'friend from front fruit full future garden general get girl give glass glove go goat gold good government grain '
              'grass great green grey grip group growth  guide gun hair hammer hand hanging happy harbour hard harmony hat hate '
              'have he head healthy hear hearing heart heat help high history hole hollow hookhope horn horse hospital hour house '
              'how humour I ice idea if ill important impulse in increase industry ink insect instrument insurance interest invention '
              'iron island jelly jewel join journey judge jump keep kettle key kick kind kiss knee knife knot knowledge land language '
              'last late laugh law  lead leaf learning leather left leg let letter level library lift light like limit line '
              'linen lip liquid list little living lock long look loose loss loud love low machine  make male man manager map mark '
              'market married  mass match material may meal measure meat medical meeting memory metal middle military milk mind '
              'mine minute mist mixed money monkey month moon morning mother motion mountain mouth move much muscle music nail '
              'name narrow nation natural near necessary neck need needle nerve net new news night no noise normal north nose not '
              'note now number nut observation of off offer office oil old on only open operation opinion opposite or orange order '
              'organization ornament other out oven over owner page pain paint paper parallel parcel part past paste payment peace '
              'pen pencil person physical picture pig pin pipe place plane plant plate play please pleasure plough pocket point '
              'poison polish political poor porter position possible pot potato powder power present price print prison private probable '
              'process produce profit property prose protest public pull pump punishment purpose push put quality question quick quiet '
              'quite rail rain range rat rate ray reaction reading ready reason receipt record red regret regular relation religion '
              'representative request respect responsible rest reward rhythm rice right ring river road rod roll roof room root '
              'rough round rub rule run sad safe sail salt same sand say scale school science scissors screw sea seat second '
              'secret secretary see seed seem selection self send sense separate serious servant shade shake shame sharp sheep '
              'shelf ship shirt shock shoe short shut side sign silk silver simple sister size skin  skirt sky sleep slip slope '
              'slow small smash smell smile smoke smooth snake sneeze snow so soap society sock soft solid some son song sort '
              'sound soup south space spade special sponge spoon spring square stage stamp star start statement station steam '
              'steel stem step stick sticky stiff still stitch stocking stomach stone stop store story straight strange street '
              'stretch strong structure substance such sudden sugar suggestion summer sun support surprise sweet swim system '
              'table tail take talk tall taste tax teaching tendency test than that the then theory there thick thin thing this '
              'thought thread throat through through thumb thunder ticket tight till time tin tired to toe together tomorrow tongue '
              'tooth top touch town trade train transport tray tree trick trouble trousers true turn twist umbrella '
              'under unit up use value verse very vessel view violent voice waiting walk wall war warm wash waste watch water wave wax '
              'way weather week weight well west wet wheel when where while whip whistle white who why wide will wind '
              'window wine wing winter wire wise with woman wood wool word work worm wound writing wrong year yellow yes yesterday '
              'ant baboon badger bat bear beaver camel cat clam cobra cougar '
              'coyote crow deer dog donkey duck eagle ferret fox frog goat '
              'goose hawk lion lizard llama mole monkey moose mouse mule newt '
              'otter owl panda parrot pigeon python rabbit ram rat raven '
              'rhino salmon seal shark sheep skunk sloth snake spider '
              'stork swan tiger toad trout turkey turtle weasel whale wolf '
              'wombat zebra '
              'you young Android ').split()
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
        death = 0
        isWin = False
        isHung = False
        final = []
        word = random.choice(random_words)
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
                UserChoice = (input('Guess a letter: ')).lower()
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


