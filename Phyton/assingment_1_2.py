from random import randint
from secrets import choice
from emoji import emojize,demojize

print (" \n Based on the following  game we designed in the class: \n")
print ("create menu-driven programming that the user can select what kind of game they want to play\n".upper())


def gameMenu ():
    # HEADER
    print("\n","".center(50, emojize(":video_game:")))
    print(" MAIN MENU ".center(100, " "))
    print("".center(50, emojize(":video_game:")))
    # MENUS
    print("\n \033[92m 1 - SINGLE PLAYER \033[0m",emojize(":video_game:"))
    print("\n \033[92m 2 - MULTIPLAYER \033[0m",emojize(":video_game:"), emojize(":VS_button:") , emojize(":video_game:"))
    print("\n \033[92m 3 - MULTIPLAYER (alternative): \033[0m", emojize(":video_game:"), emojize(":VS_button:") , emojize(":video_game:"))
    print("\n \033[92m 4 - exit \033[0m ",emojize(":door:"))
    return input("\n \033[92m Select the menu : (1,2,3, 4) : \033[0m")

def menu_choice():
    while True:
        choice = gameMenu()
        if choice == "1": 
            print("\033[33m You choose SINGLE PLAYER \033[0m")
            singlePlayer()
        elif choice == "2": 
            print("\033[33m You choose MULTIPLAYER \033[0m")
            pass
        elif choice == "3": 
            print("\033[33m You choose MULTIPLAYER alternative \033[0m")
            multiplayerAlt()
        elif choice == "4": 
            print("\033[33m Thanks for using my first game in Python.... \033[0m", emojize(":waving_hand:"))
            break
        else:
            print("\n \033[91m BAD INPUT, PLEASE TRY AGAIN \033[0m", emojize(":cross_mark:"))


def singlePlayer(): # Single player Gessing Game
    print (" \n \033[92m In this game you need to guess the number between 1 and 100 Generated by the computer \033[0m")
    # randNum = randint(1,100) 
    randNum = randint(1,2) # testing
    counter = 0

    while True:
        guess = int(input(" \033[92m Type a number: \033[0m"))
        # guess = 1 testing
        counter += 1
        if guess < randNum :
            print(" \033[91m Sorry try again, Something bigger this time \033[0m")
        elif guess > randNum:
            print("\033[91m Sorry try again, Something smaller this time \033[0m" )
        else:
            print(" \033[1;32;40m CONGRATULATIONS!!! \033[m".ljust(40,emojize(":confetti_ball:")))
            print(f" \033[1;32;40m YOU WIN WITH {counter} TRIES \033[m")
            break 

def multiplayerAlt ():
    print (" \n \033[92m In this game you need to guess the number between 1 and 100 Generated by the computer \033[0m")
    print (" \n \033[92m When one of you get a wrong guess give the the other player will start  \033[0m")

    player1 = input("Type the Player 1 name: ")
    player2 = input("Type the Player 2 name: ")
    # randNum = randint(1,100) 
    randNum = randint(1,2) 
    counterPlay1 = 0
    counterPlay2 = 0
    turn = player1
    rounds = 0 

    while rounds < 4 :
        rounds += 1 
        if turn == player1:
            print(f"{player1} is our turn:")
            guess = int(input(" \033[92m Type a number: \033[0m"))

            if guess < randNum :
                print("\033[91m Sorry try again, Something bigger this time \033[0m")
                turn = player2
            elif guess > randNum:
                print("\033[91m Sorry try again, Something smaller this time \033[0m" )
                turn = player2
            else:
                counterPlay1 += 1
                print(f"\033[1;32;40m CONGRATULATIONS!!! {player1} YOU  GOT IT. \033[m".ljust(40,emojize(":confetti_ball:")))
                randNum = randint(1,2) 
                turn = player2
            
        else:
            print(f"{player2} is our turn:")
            guess = int(input(" \033[92m Type a number: \033[0m"))

            if guess < randNum :
                print("\033[91m Sorry try again, Something bigger this time \033[0m")
                turn = player1
            elif guess > randNum:
                print("\033[91m Sorry try again, Something smaller this time \033[0m" )
                turn = player1
            else:
                counterPlay2 += 1
                print(f"\033[1;32;40m CONGRATULATIONS!!! {player2} YOU  GOT IT. \033[m".ljust(40,emojize(":confetti_ball:")))
                randNum = randint(1,2) 
                turn = player1

    if counterPlay1 > counterPlay2:
        print(f"win {player1}")
    elif counterPlay1 > counterPlay2:
        print(f"win {player2}")
    else:
        print(f"is a TIE")

multiplayerAlt()