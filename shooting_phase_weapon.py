weapon_list = []            # list all weapons will be stored in

stats_list = []

p = 1

w = 0

while p == 1:
    print("Weapons", weapon_list)
    weapon_location = eval(input("If weapon was on list enter: 1 \nIf weapon was not on list enter: 2 \nIf you are finished enter: 3\nEnter: "))  # If weapon is in list ask for what weapon it was. If not get a new weapon appended onto the list.
    print(weapon_location)
    if weapon_location == 1:
        print("Weapons", weapon_list)
        weapon = eval(input("What weapon is being fired\ne.g. weapon first in list is 1\nWeapon: "))

    elif weapon_location == 2:
        new_weapon = input("What is your weapon called: ")
        capital_weapon = new_weapon.capitalize()
        weapon_list.append([])                # makes a list in the weapon list then appends the new weapon to the new list.
        weapon_list[w].append(capital_weapon)
        weapon_s = eval(input("What is the weapons strength:"))                             # weapon strength armour pierce and damage
        weapon_ap = eval(input("What is the weapons armour pierce:"))
        weapon_d = eval(input("What is the weapons damage:"))
        stats_list.append([])
        stats_list[w].append(weapon_s)
        stats_list[w].append(weapon_ap)
        stats_list[w].append(weapon_d)
        print("Stats", stats_list[w])
        print("Weapons", weapon_list,"\n\n")
        w += 1
    elif weapon_location == 3:
        break
    else:
        print("Please enter a different value")
