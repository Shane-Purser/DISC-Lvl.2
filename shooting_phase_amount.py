import random

amount_rolled = 0

rolled_numbers = []

game = 1


def roll_dice(side_of_dice, number_of_dice):         # Function that has the code needed to roll certain sided dice a certain number of times
    while number_of_dice >= 1:        # While loop controls the amount of time the 3 or 6 sided dice is rolled
        if side_of_dice == 3:                        # If ,Elif and Else code to pick whether the number entered is valid or if the code should ask for a different input value
            n = random.randint(1, 3)
            rolled_numbers.append(n)
        elif side_of_dice == 6:
            n = random.randint(1, 6)
            rolled_numbers.append(n)
        else:
            print("Please enter a different value")
            break
        number_of_dice -= 1
    print("you rolled these numbers:", rolled_numbers)


def select_weapon():

    weapon_list = []            # list all weapons will be stored in

    w_stats_list = []

    w_name_list = []

    p = 1

    w = 0

    while p == 1:
        print("Weapons", w_name_list)
        weapon_location = eval(input("If weapon was on list enter: 1 \nIf weapon was not on list enter: 2 \nIf you are finished enter: 3\nEnter: "))  # If weapon is in list ask for what weapon it was. If not get a new weapon appended onto the list.
        if weapon_location == 1:
            print("Weapons", w_name_list)
            weapon = eval(input("What weapon is being fired\ne.g. weapon first in list is 1\nWeapon: "))
            print(weapon_list[weapon - 1], "\nIs this the correct weapon\n")
            confirm = eval(input("if this is your weapon enter: 1\nIf this is not your weapon enter: 2\n enter: "))
            if confirm == 1:
                return weapon_list[weapon - 1]
            if confirm != 1:
                print("This is not a valid answer. Please enter a different value.")

        elif weapon_location == 2:
            new_weapon = input("What is your weapon called: ")
            capital_weapon = new_weapon.capitalize()
            w_name_list.append([])                # makes a list in the weapon list then appends the new weapon to the new list.
            w_name_list[w].append(capital_weapon)
            weapon_s = eval(input("What is the weapons strength:"))                             # weapon strength armour pierce and damage
            weapon_ap = eval(input("What is the weapons armour pierce:"))
            weapon_d = eval(input("What is the weapons damage:"))
            w_stats_list.append([])
            w_stats_list[w].append(weapon_s)
            w_stats_list[w].append(weapon_ap)
            w_stats_list[w].append(weapon_d)
            print("Stats", w_stats_list[w])
            print("Weapons", w_name_list, "\n\n")
            weapon_list.append([])
            weapon_list[w].append(capital_weapon)
            weapon_list[w].append(weapon_s)
            weapon_list[w].append(weapon_ap)
            weapon_list[w].append(weapon_d)
            w += 1
        elif weapon_location == 3:
            break
        else:
            print("Please enter a different value")


while game == 1:
    print("Welcome to the Shooting phase")
    selected_weapon = select_weapon()
    dice_sides = eval(input("Please enter in numbers e.g. 3, 6 \n How many sides to the dice:"))     # These two lines are used to make the roll_dice function look tidier when it is called on
    dice_number = eval(input("How many dice are you rolling: "))
    if dice_sides == 3:
        roll_dice(dice_sides, dice_number)
        total_amount = sum(rolled_numbers)
        print("You rolled a total of:", total_amount)
    if dice_sides == 6:
        roll_dice(dice_sides, dice_number)
        total_amount = sum(rolled_numbers)
        print("You rolled a total of:", total_amount)
