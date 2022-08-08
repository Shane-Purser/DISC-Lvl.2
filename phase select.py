activity = 1


def play(phase, game_state):
    while game_state == 1:
        if phase == 1:
            print("Psychic\n\n")
            break
        elif phase == 2:
            print("Shooting\n\n")
            break
        elif phase == 3:
            print("Thank ou for playing!!")
            break
        else:
            print("Phase name was not recognised \n Please enter a different phase\n\n")


while activity == 1:
    phase_select = eval(input(
        "Are you in a Psychic phase, Shooting phase or are you Finished \n please enter one of these options using the numbers e.g. 1, 2, 3 \nPsychic(1)\nShooting(2)\nFinished(3) \n Phase:"))
    play(phase_select, 1)
    if phase_select == 3:
        activity -= 1
