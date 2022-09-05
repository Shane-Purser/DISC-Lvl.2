import random

p = 1

final_troop_list = []

final_weapon_list = []

while p == 1:
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
        w = 0
        weapon_list = []            # list all weapons will be stored in

        w_stats_list = []

        w_name_list = []

        g = 1
        while g == 1:
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
                print("Thanks for playing")
            else:
                print("Please enter a different value")


    def troop_select():

        troop_list = []            # list all weapons will be stored in

        t_stats_list = []

        t_name_list = []

        w = 0

        while p == 1:
            print("Troops", t_name_list)
            troop_location = eval(input("If troop was on list enter: 1 \nIf troop was not on list enter: 2 \nIf you are finished enter: 3\nEnter: "))  # If troop is in list ask for what troop it was. If troop not on list get a new troop appended onto the list.
            if troop_location == 1:
                print("Troops", t_name_list)
                troop = eval(input("What troop is being used\ne.g. troop first in list is 1\nTroop: "))
                print(troop_list[troop - 1], "\nIs this the correct Troop")
                confirm = eval(input("if this is your troop enter: 1\nIf this is not your troop enter: 2\n enter: "))
                if confirm == 1:
                    return troop_list[troop - 1]
                if confirm != 1:
                    print("This is not a valid answer. Please enter a different value.")

            elif troop_location == 2:
                new_troop = input("What is your Troop called: ")
                capital_weapon = new_troop.capitalize()
                t_name_list.append([])                # makes a list in the troop list then appends the new troops name to the new list.
                t_name_list[w].append(capital_weapon)
                troop_ws = eval(input("What is the troops weapon skill:"))                             # troop stats
                troop_bs = eval(input("What is the troops ballistic skill:"))
                troop_s = eval(input("What is the troops strength:"))
                troop_t = eval(input("What is the troops toughness:"))
                troop_w = eval(input("What is the troops wounds:"))
                troop_a = eval(input("What is the troops attack:"))
                troop_ld = eval(input("What is the troops leadership:"))
                troop_sv = eval(input("What is the troops save:"))
                troop_iv = eval(input("What is the troops invulnerable(if none enter 0):"))
                t_stats_list.append([])
                t_stats_list[w].append(troop_ws)
                t_stats_list[w].append(troop_bs)
                t_stats_list[w].append(troop_s)
                t_stats_list[w].append(troop_t)
                t_stats_list[w].append(troop_w)
                t_stats_list[w].append(troop_a)
                t_stats_list[w].append(troop_ld)
                t_stats_list[w].append(troop_sv)
                t_stats_list[w].append(troop_iv)
                print("Stats", t_stats_list[w])
                print("Troops", t_name_list, "\n\n")
                troop_list.append([])
                troop_list[w].append(capital_weapon)
                troop_list[w].append(troop_ws)
                troop_list[w].append(troop_bs)
                troop_list[w].append(troop_s)
                troop_list[w].append(troop_t)
                troop_list[w].append(troop_w)
                troop_list[w].append(troop_a)
                troop_list[w].append(troop_ld)
                troop_list[w].append(troop_sv)
                troop_list[w].append(troop_iv)
                w += 1
            elif troop_location == 3:
                break
            else:
                print("Please enter a different value")


    while game == 1:
        i = 0
        hits = 0
        loop = 2
        while loop >= 1:
            loop = 2
            print("\n\nWelcome to the Shooting phase")
            print(final_weapon_list)
            o = eval(input("If your weapon is on he list enter: 1\nIf your weapon is not on the list enter:2\nEnter:"))
            if o == 2:
                selected_weapon = select_weapon()
                final_weapon_list.append(selected_weapon)
                print("You have selected ", selected_weapon, "\n\n")
                loop -= 1
            elif o == 1:
                used_weapon = eval(input("What weapon are you using from the list. \nFirst weapon on list is 1 next is 2 esc. \nWeapon:"))
                selected_weapon = final_weapon_list[used_weapon - 1]
                loop -= 1
            else:
                print("That is not a valid input. Please try again")

            m = eval(input("If your weapon is on he list enter: 1\nIf your weapon is not on the list enter:2\nEnter:"))
            if m == 2:
                selected_troop = troop_select()
                final_troop_list.append(selected_troop)
                print("You have selected", selected_troop, "\n\n")
                loop -= 1
            elif m == 1:
                used_troop = eval(input("What troop are you using from the list. \nFirst troop on list is 1 next is 2 esc. \nTroop:"))
                selected_troop = final_troop_list[used_troop - 1]
                loop -= 1
            else:
                print("That is not a valid input. Please try again")
        dice_sides = eval(input("Please enter in numbers e.g. 3, 6 \nHow many sides to the dice:"))     # These two lines are used to make the roll_dice function look tidier when it is called on
        dice_number = eval(input("How many dice are you rolling: "))
        ballistic_skill = selected_troop[2]
        if dice_sides == 3:
            roll_dice(dice_sides, dice_number)
            for numbers in rolled_numbers:
                if rolled_numbers[i] >= ballistic_skill:
                    hits += 1
                i += 1
            print("You hit the target", hits, " times")
        if dice_sides == 6:
            roll_dice(dice_sides, dice_number)
            for numbers in rolled_numbers:
                if rolled_numbers[i] >= ballistic_skill:
                    hits += 1
                i += 1
            print("You hit the target", hits, " times")
