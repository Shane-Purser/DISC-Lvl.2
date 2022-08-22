def play():    # Function that will run all main phases of the game
    phase = eval(input("What phase do you want to play\nIf shooting enter: 1\n If psychic enter: 2\n If you wish to exit enter: 3"))
    if phase == 1:
        return 1
    elif phase == 2:
        return 2
    elif phase == 3:
        return 3
    else:
        print("Phase name was not recognised \n Please enter a different phase\n")


game_state = play()
if game_state == 1:  # run the shooting phase


if game_state == 2: # run the psychic phase


if game_state == 3: # stop the code from running
    print("Thanks for playing!!")
