
import time

print(r"                .____   __ _    ")
print(r"                   __o__   _______ _ _  _                                     /     /     ")
print(r"                   \    ~\                                                  /      /      ")
print(r"                     \     '\                                         ..../      .'          ")
print(r"                      . ' ' . ~\                                      ' /       /             ")
print(r"                     .  _    .  ~ \  .+~\~ ~ ' ' " " ' ' ~ - - - - - -''_      /               ")   
print(r"                    .  <#  .  - - -/' . ' \  __                          '~ - \               ")
print(r"                     .. -           ~-.._ / |__|  ( )  ( )  ( )  0  o    _ _    ~ .           ")
print(r"                   .-'                                               .- ~    '-.    -.        ")
print(r"                  <                      . ~ ' ' .             . - ~             ~ -.__~_. _ _ ")
print(r"                    ~- .       N121PP  .          . . . . ,- ~                                    ")  
print(r"                         ' ~ - - - - =.   <#>    .         \.._                                  ") 
print(r"                                     .     ~      ____ _ .. ..  .- .                             ")
print(r"                                       .         '        ~ -.        ~ -.                           ")
print(r"                                         ' . . '               ~ - .       ~-.                        ")
print(r"                                                                     ~ - .      ~ .                   ") 
print(r"                                                                          ~ -...0..~. ____             ")
time.sleep(2)
print("\n     *****--------------------------------------------------------------------------------------------------------------*****")


print(r"      ________  ___________   ___________________ ___   .___ _______    ______________ ______________    _____  ._____________   ")
print(r"      \______ \ \_   _____/  /  _  \__    ___/   |   \  |   |\      \   \__    ___/   |   \_   _____/   /  _  \ |   \______   \ ")
print(r"       |    |  \ |    __)_  /  /_\  \|    | /    ~    \ |   |/   |   \    |    | /    ~    \    __)_   /  /_\  \|   ||       _/  ")
print(r"       |    `   \|        \/    |    \    | \    Y    / |   /    |    \   |    | \    Y    /        \ /    |    \   ||    |   \   ")
print(r"      /_______  /_______  /\____|__  /____|  \___|_  /  |___\____|__  /   |____|  \___|_  /_______  / \____|__  /___||____|_  /    ")
print(r"              \/        \/         \/              \/               \/                  \/        \/          \/            \/     ")       
print(r"                                                                                                                                   ")

print("  \n        ***-------------------------------------------------------------------------------------------------------------***")

#------------------------------------------------------------

time.sleep(2)
print("\nYou awake in your plane seat.")
time.sleep(2)
print("\nYou're confused but notice two stewardesses several rows in front.")
time.sleep(2)
print("\nThey appear extremely concerned and distrought.")
time.sleep(2)
print("\nWhat do you do?\n")
time.sleep(2)

#OPTIONS
print("1/ Ask the lady next to you what is happening.\n")
print("2/ Ask the stewardesses about it.\n")
print("3/ Do some investigating yourself (look in peoples' bags).\n")

#OPTIONINPUT

def choice1_1():
    print("Option 1.1 selected")

def choice1_2():
    print("Option 1.2 selected")

def choice1_3():
    print("Option 1.3 selected")

def choice1():

    choiceinputted2 = False

    while(choiceinputted2 == False):
        print("You smile at the lady and try to impress on her that everything will be fine.")
        print("'The staff on flights have to be mindful about security, I'm sure it's nothing.'\n")
        print("The lady calms down.")
        print("'Sorry about that, my name's Jean.")
        print("Everyone on te plane received a really horrid text from an unknown number.")
        print("The airline are taking it seriously by the sounds of it.")
        print("Everyone's worried. I'm definitely worried.\n")
        print("She shows you the text..\n")
        print("'GREETINGS FELLOW TRAVELLERS")
        print("I HAVE BECOME INCREASINGLY AWARE RECENTLY OF THE EPENDABLE NATURE OF HUMANITY")
        print("WE ARE CATTLE - WE ARE HEARDED AND WE ARE MILKED OF OUR GOODNESS, LEAVING US HOLLOW SHELLS.")
        print("NOW IS THE TIME I DEMONSTRATE MY WORTH.")
        print("I AM IN POSSESSION OF A PARTICULARLY POWERFUL INCENDIARY DEVICE THAT WILL BE")
        print("DETONATED OVER HEATHROW AIRPORT UNLESS I AM GIVEN WHAT. I. WANT.")
        print("\nYOURS SINCERELY,\n")
        print("A REVOLUTIONARY\n")

        print("What do you do next?\n")
        print("1/ Reassure her.\n")
        print("2/ Ignore her 'ramblings'\n")
        choicevalue2 = input("Enter your choice: ")

        if(choicevalue2 == "1"):
            print()
            choiceinputted2 = True

            choice1_1()
            
        elif(choicevalue2 == "2"):
            print("\nThe bag itself is empty apart from a phone, a beaten up old Samsung.\n")
            print("What do you do next?\n")
            choiceinputted2 = True

            choice1_2()

        elif(choicevalue2 == "3"):
            print("\nThere is a new laptop and it's charger, plus a wedding ring inscribed with Farsi and some 'foreign' food.\n")
            print("What do you do next?\n")
            choiceinputted2 = True

            choice1_3()

        else:
            print("\nYou need to choose 1, 2 or 3.\n")

def choice2():
    print("Choice 2.0 selected")

def choice3():
    print("Choice 3.0 selected")

def main():

    choiceinputted = False

    while(choiceinputted == False):
        choicevalue = input("Enter your choice: ")

        if(choicevalue == "1"):
            print("You ask the lady next to you what has happened..\n")
            print("The lady stammers 'We've b-be-been.. w-we're going to be bombed!\n")
            time.sleep(2)
            print("I have two kids at home!\n")
            time.sleep(2)
            print("She bursts into tears.")
            time.sleep(2)
            choiceinputted = True

            choice1()
            
        elif(choicevalue == "2"):
            print("You approach the stewardesses and ask them to explain what is happening..\n")
            print("\nThe taller of the stewardesses glares at you and through gritted teeth,\n")
            time.sleep(2)
            print("she orders you to sit back down.")
            time.sleep(2)
            print("And make sure to fasten your seatbelt as well!\n")
            time.sleep(2)
            choiceinputted = True

            choice2()

        elif(choicevalue == "3"):
            print("You decide to find out for yourself what is going on.\n")
            time.sleep(2)
            print("You surreptitiously search the bags in the same overheard locker as you.")
            time.sleep(2)
            choiceinputted = True

            choice3()

        else:
            print("\nYou need to choose 1, 2 or 3.\n")

main()