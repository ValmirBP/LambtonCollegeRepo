from emoji import emojize

print (" \n Based on the following  game we designed in the class: \n")
print ("create menu-driven programming that the user can select what kind of game they want to play\n".upper())

def game_menu ():
    print(" MAIN MENU".center(50, emojize(":video_game:")))
    print('1 - SINGLE PLAYER')
    print('2 - MULTIPLAYER')
    print('3 - play the game two player (alternative): ')
    print('4 - exit')
    return input('Select the menu : (1,2,3, 4) : ')


