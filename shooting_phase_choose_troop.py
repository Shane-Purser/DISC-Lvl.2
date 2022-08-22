def troop_select():

    troop_list = []            # list all weapons will be stored in

    t_stats_list = []

    t_name_list = []

    p = 1

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


selected_troop = troop_select()
