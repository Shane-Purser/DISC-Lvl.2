import random

def roll_dice():
    side_of_die = input("Are you using three sided dice or six \n For a 3 sided die enter: Three \n For a 6 sided die enter: Six \n Enter:")
    capatilise_string = side_of_die.capitalize()


    if capatilise_string == "Three":
        n = random.randint(1,3)
        print(n)
    elif capatilise_string == "Six":
        n = random.randit(1,6)
        print(n)
    else:
        print("Please enter a different value")
roll_dice()
