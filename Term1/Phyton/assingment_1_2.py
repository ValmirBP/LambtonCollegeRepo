from random import randint
from secrets import choice
from time import sleep
from emoji import emojize
class color:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightGrey = '\033[37m'
        darkGrey = '\033[90m'
        lightRed = '\033[91m'
        lightGreen = '\033[92m'
        yellow = '\033[93m'
        lightBlue = '\033[94m'
        pink = '\033[95m'
        lightCyan = '\033[96m'
        reset = '\033[0m'

print(color.red,"\n Based on the following  game we designed in the class:",color.reset)
print(color.green,"create menu-driven programming that the user can select what kind of game they want to play\n".upper(),color.reset)

# Guessing game Single Player OPT 1
def singlePlayer(): 
    print(color.blue, "In this game you need to guess the number between 1 and 10 Generated by the computer\n", color.reset)
    randNum = randint(1,10) 
    counter = 0

    while True:
        guess = int(input(" Type a number:"))
        counter += 1

        if guess < randNum :
            print(color.red," \n Sorry try again, Something bigger this time", color.reset)
        elif guess > randNum:
            print(color.red, "\n Sorry try again, Something smaller this time", color.reset)
        else:
            print(color.cyan, " CONGRATULATIONS!!!",color.reset.ljust(6,emojize(":confetti_ball:")))
            print(color.cyan, f" YOU WIN WITH {counter} TRIES", color.reset)
            break 
# Guessing game Multiplayer OPT 2
def playMultiplayer2():

    print(color.blue, "\n In this game you need to guess the number between 1 and 10 Generated by the computer\n", color.reset)
    print(color.blue, "Rules: \n 1 - The player that will start is random \n 2 - Each player will play the game 1 time", color.reset)
    print(color.blue, "3 - Each game has 4 rounds \n 4 - The player that has more hits wins \n", color.reset)

    player1 = input("Type the Player 1 name: ").strip()
    player2 = input("Type the Player 2 name: ").strip()
    playerLst = [player1,player2]
    randPlayer = choice(playerLst)
    turn = randPlayer
    player1wins = 0
    player2wins = 0
    gamePlayed = 0 

    def multiplayer():
        winner = 0
        gameRound = 0
        randNum = randint(1,10) 

        while gameRound < 4:
            gameRound +=1
            guess = int(input(" Type a number:"))
            
            if guess < randNum :
                print(color.red, "\n Sorry try again, Something bigger this time \n", color.reset)
            elif guess > randNum:
                print(color.red,"\n Sorry try again, Something smaller this time \n", color.reset )
            else:
                winner += 1
                randNum = randint(1,10) 
                print(color.cyan,f"\n CONGRATULATIONS!!! {randPlayer} YOU GOT IT!!!.",color.reset.ljust(7,emojize(":confetti_ball:")))
        return winner, gameRound
        
    while True:
        if gamePlayed <= 1:
            if turn == player1:
                print(color.green,f"\n {player1} is our turn:\n", color.reset)
                player1wins,gameRounds = multiplayer()
        
                if gameRounds <= 4:
                    gamePlayed += 1
                    turn = player2

            elif turn == player2:
                print(color.green,f"\n {player2} is our turn:\n", color.reset)
                player2wins,gameRounds = multiplayer()
                if gameRounds <= 4:
                    gamePlayed += 1
                    turn = player1
        else:
            break

    if player1wins > player2wins:
        print(color.cyan,f"\n THE WINNER IS...",color.reset)
        sleep(1.5)
        print(color.cyan,f"\n {player1} CONGRATULATIONS!!!",color.reset.ljust(7,emojize(":confetti_ball:")))
        print(color.cyan,f"\n YOU GOT {player1wins} RIGHT GUESSES !!!.",color.reset.ljust(7,emojize(":confetti_ball:")))
    elif player1wins < player2wins:
        print(color.cyan,f"\n THE WINNER IS...",color.reset)
        sleep(1.5)
        print(color.cyan,f"\n {player2} CONGRATULATIONS!!!",color.reset.ljust(7,emojize(":confetti_ball:")))
        print(color.cyan,f"\n YOU GOT {player2wins} RIGHT GUESSES !!!.",color.reset.ljust(7,emojize(":confetti_ball:")))
    else:
        print(color.cyan,f"\n IT IS A TIE !!!.",color.reset)
# Guessing game Multiplayer Alternative OPT 3
def playMultilayerAlt():

    print(color.blue, "\n In this game you need to guess the number between 1 and 10 Generated by the computer\n", color.reset)
    print(color.blue, "Rules: \n 1 - The player that will start is random \n 2 - Each player will play alternately ", color.reset)
    print(color.blue, "3 - The player that has hits first wins \n ", color.reset)
    
    randNum = randint(1,10) 
    player1 = input("Type the Player 1 name: ").strip()
    player2 = input("Type the Player 2 name: ").strip()
    playerLst = [player1,player2]
    randPlayer = choice(playerLst)
    turn = randPlayer

    def multiplayerAlt():
        winner = 0
        guess = int(input(" Type a number:"))
        
        if guess < randNum :
            print(color.red, "\n Sorry try again, Something bigger this time \n", color.reset)
        elif guess > randNum:
            print(color.red,"\n Sorry try again, Something smaller this time \n", color.reset )
        else:
            winner += 1
            print(color.cyan,f"\n CONGRATULATIONS!!! {turn} YOU WIN!!!.",color.reset.ljust(7,emojize(":confetti_ball:")))
        return winner

    while True:
        if turn == player1:
            print(color.green,f"\n {player1} is our turn:\n", color.reset)
            winner = multiplayerAlt()
            if winner == 1:
                break
            turn = player2
        else:
            print(color.green, f"\n {player2} is our turn: \n ",color.reset)
            winner = multiplayerAlt()
            if winner == 1:
                break
            turn = player1
# MENU GENERATED 
def gameMenu():
    # HEADER
    print("".center(50, emojize(":video_game:")))
    print(color.lightGreen, " MAIN MENU ".center(100, " "), color.reset)
    print("".center(50, emojize(":video_game:")))
    # MENUS
    print(color.blue, "\n 1 - SINGLE PLAYER",emojize(":video_game:"),color.reset)
    print(color.blue, "\n 2 - MULTIPLAYER",emojize(":video_game:"), emojize(":VS_button:"), emojize(":video_game:"), color.reset)
    print(color.blue, "\n 3 - MULTIPLAYER(alternative):", emojize(":video_game:"), emojize(":VS_button:") , emojize(":video_game:"), color.reset)
    print(color.yellow, "\n 4 - exit ",emojize(":door:"),color.reset)
    return input("\n Select the menu :(1,2,3, 4) :")
# MENU FUNCTION 
def menuChoice():
    while True:
        choice = gameMenu()

        if choice == "1": 
            print(color.red, "\n You choose SINGLE PLAYER \n", color.reset)
            singlePlayer()

        elif choice == "2": 
            print(color.red, "\n You choose MULTIPLAYER \n", color.reset)
            playMultiplayer2()

        elif choice == "3": 
            print(color.red, "\n You choose MULTIPLAYER alternative \n", color.reset)
            playMultilayerAlt()

        elif choice == "4": 
            print(color.lightGreen, "\n Thanks for using my first game in Python....", emojize(":waving_hand:"), color.reset)
            break

        else:
            print(color.red, "\n BAD INPUT, PLEASE TRY AGAIN", emojize(":cross_mark:"), color.reset)

# Execution  of the game
menuChoice()