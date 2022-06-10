import random


# creating a list.
#
RPS_game = ['R', 'P', 'S']
# print(RPS_game)

isValidOptionSelected = False
print("Welcome to the Rock-Paper-Scissors game!")
print('''
You are to choose between the following letters:
R, P and S.

R = Rock
P = Paper
S = Scissors

''')


def init():

    while isValidOptionSelected == False:

        playerChoice = input("Please pick anyone of the letters : \n")
        compChoice = random.choice(RPS_game)

        if (playerChoice == compChoice):
            print('Player (' + playerChoice + '): CPU (' + compChoice + ')')
            print("Its is a Tie! We go again")

        elif (playerChoice == 'R'):
            isValidOptionSelected == True
            if (compChoice == 'S'):

                print("Player (Rock) : CPU (Scissors)")
                print('You win! Rock beats Scissors!')
                Endgame()
                break
            else:
                print('Player (Rock) : CPU (Paper)')
                print("CPU win! Paper beats Rock!")
                Endgame()
                break

        elif (playerChoice == 'P'):
            isValidOptionSelected == True
            if (compChoice == 'R'):
                print("Player (Paper) : CPU (Rock)")
                print('You win! Paper beats Rock!')
                Endgame()
                break
            else:
                print("Player (Paper) : CPU (Scissors)")
                print("CPU win! Scissors beats Paper!")
                Endgame()
                break

        elif (playerChoice == 'S'):
            isValidOptionSelected == True
            if (compChoice == 'P'):
                print('Player (Scissors) : CPU (Paper)')
                print("CPU win! Scissors beats Paper!")
                Endgame()
                break
            else:
                print('Player (Scissors) : CPU (Rock)')
                print("CPU win! Rock beats Scissors!")
                Endgame()
                break
        else:
            print('Your input is invalid, please try again')


def Endgame():
    print("********* END OF GAME! *********")

    print('----------- GOODBYE -----------')


init()
