import random

dice_sides = eval(input("Please enter in numbers e.g. 3, 6 \n How many sides to the dice:"))     # These two lines are used to make the roll_dice function look tidier when it is called on
dice_number = eval(input("Please enter in numbers e.g. 1, 2, 3 \n How many dice: "))


def roll_dice(side_of_dice, number_of_dice):         # Function that has the code needed to roll certain sided dice a certain number of times
    while number_of_dice >= 1:                       # While loop controls the amount of time the 3 or 6 sided dice is rolled
        if side_of_dice == 3:                        # If ,Elif and Else code to pick whether the number entered is valid or if the code should ask for a different input value
            n = random.randint(1, 3)
            print(n)
        elif side_of_dice == 6:
            n = random.randint(1, 6)
            print(n)
        else:
            print("Please enter a different value")
        number_of_dice -= 1


roll_dice(dice_sides, dice_number)
