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
