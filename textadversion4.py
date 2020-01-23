
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
print(r"                    ~- .    SWISS AIR  .          . . . . ,- ~                                 ")  
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

def choice1_1_1():
    
    choiceinputted = False

    while(choiceinputted == False):

        print("What do you do next?\n")
        time.sleep(2)
        print("1/ Rummage through the bags of the suspects.\n")
        print("2/ Mention this information to the stewards and suggest we search people.")
        print("   (Doctor 16A, young lady 16C, Asian guy front row for that specific phone)\n")
        print("3/ Scare the individuals into 'confessing'.\n")
        choiceinputted = True

def choice1_1_2():
    print("\n")
def choice1_1_3():
    print("\nFinal choice so far")

def choice1_1():
    
    choiceinputted = False

    while(choiceinputted == False):
        print("")

        print("What do you do next?\n")
        time.sleep(2)
        print("1/ Use your limited tech skills to attempt to trace the phone.\n")
        print("2/ Ask the lady next to you for more details.\n")
        print("3/ Demand to speak to the pilot. Harass the stewards.\n")
        choicevalue = input("Enter your choice: ")

        if (choicevalue == "1"):

            print("\nYou use your limited skills to attempt to trace the phone.")
            time.sleep(2)
            print("Unfortunately you do not get far, but you realise a couple of things from the signature of the sent text.\n")
            time.sleep(2)
            print("It was sent from a sony xperia Z5.\n")
            time.sleep(2)
            print("The person is clearly educated and can spell.\n")
            time.sleep(2)
            print("You realise this is important as it must eliminate some people from your thought process.\n")
            time.sleep(2)

            choiceinputted = True

            choice1_1_1()

        if (choicevalue == "2"):

            print("\nYou ask the lady what else she knows about it.")
            time.sleep(2)
            print("She points them out -")
            time.sleep(2)
            print("- The well dressed gentleman in seat 16A (looks like a Doctor).")
            time.sleep(2)
            print("- The lady two seats down from him in 16C, she's young and looks like she relies on her looks for her job (extensions, hair and eyelash + painted nails).")
            time.sleep(2)
            print("- The gentleman in the front row (Asian) who appears to be with his family.")
            time.sleep(2)
            print("- Oh and both Stewardesses had their phones out. Probably putting them on silent/airplane mode for the journey ahead.")
            time.sleep(2)
            print("The Doctor gentleman looks round at you alarmed.")
            time.sleep(2)
            print("You hear a loud beeping.\n")
            time.sleep(2)
            print("Everything else goes quiet around you suddenly.\n")
            time.sleep(2)
            print("Sound returns like a tidal wave and you feel a momentary searing pain before you are blasted into oblivion.\n")
            time.sleep(2)
            print("Oops, YOU DIED! Should be more careful about what you say.\n")
            time.sleep(2)

            choice1_1_2()

        if(choicevalue == "3"):

            print("\nYou get up close and personal with both stewardesses who demand you return to your seat.\n")
            print("You continue to demand answers and the guy who you think is a Doctor marches up to you and injects a syringe of liquid directly into your arm.\n")
            print("You start to feel faint and are directed to sit down in your seat again.\n")

            choice1_1_3()


def choice1_2():
    print("Option 1.2 selected")

def choice1_3():
    print("Option 1.3 selected")

def choice1():

    choiceinputted = False

    while(choiceinputted == False):
        print("-------------------------------------------------------------------------------------------------------------***")
        time.sleep(2)
        print("What do you do next?\n")
        print("1/ Reassure her.\n")
        print("2/ Ignore her 'ramblings'\n")
        time.sleep(2)
        choicevalue = input("Enter your choice: ")

        if(choicevalue == "1"):

            print("\nYou smile at the lady and try to impress on her that everything will be fine.\n")
            time.sleep(2)
            print("'The staff on flights have to be mindful about security, I'm sure it's nothing.'\n")
            time.sleep(2)
            print("The lady calms down.\n")
            time.sleep(2)
            print("'Sorry about that, my name's Jean.\n")
            time.sleep(2)
            print("Everyone on te plane received a really horrid text from an unknown number.\n")
            time.sleep(2)
            print("The airline are taking it seriously by the sounds of it.\n")
            time.sleep(2)
            print("Everyone's worried. I'm definitely worried.\n")
            time.sleep(2)
            print("She shows you the text..\n")
            time.sleep(2)
            print("'GREETINGS FELLOW TRAVELLERS\n")
            time.sleep(2)
            print("I HAVE BECOME INCREASINGLY AWARE RECENTLY OF THE EPENDABLE NATURE OF HUMANITY\n")
            time.sleep(2)
            print("WE ARE CATTLE - WE ARE HEARDED AND WE ARE MILKED OF OUR GOODNESS, LEAVING US HOLLOW SHELLS.\n")
            time.sleep(2)
            print("NOW IS THE TIME I DEMONSTRATE MY WORTH.\n")
            time.sleep(2)
            print("I AM IN POSSESSION OF A PARTICULARLY POWERFUL INCENDIARY DEVICE THAT WILL BE\n")
            time.sleep(2)
            print("DETONATED OVER HEATHROW AIRPORT UNLESS I AM GIVEN WHAT. I. WANT.\n")
            time.sleep(2)
            print("\nYOURS SINCERELY,\n")
            time.sleep(2)
            print("A REVOLUTIONARY\n")
            time.sleep(2)

            choiceinputted = True

            choice1_1()
            
        elif(choicevalue == "2"):

            print("\nYou give the lady a look as if to say - 'You're insane!'\n")
            time.sleep(2)
            print("Following that, you relocate to another seat to get away from the lady.\n")
            time.sleep(2)
            print("While changing seats, you feel an incredibly heavy blow to the back of your head.\n")
            time.sleep(2)
            print("You lose consciousness and wake up some time later.\n")
            time.sleep(2)
            print("Your hands and feet are bound and you appear to be in the cargo hold.\n")
            time.sleep(2)

            choiceinputted = True

            choice1_2()

        else:
            print("\nYou need to choose 1, 2 or 3.\n")

def choice2():
    print("-------------------------------------------------------------------------------------------------------------***")
    time.sleep(2)
    print("What do you do now?\n")
    time.sleep(2)
    print("1/ Do as she says.\n")
    time.sleep(2)
    print("2/ Tell her you are with the airforce and can help her with her enquiries.\n")
    time.sleep(2)

    choiceinputted = False

    while(choiceinputted == False):
        choicevalue = input("Enter your choice: ")

        if(choicevalue == "1"):
            print("You sit back down in your seat and sigh, you seem to be getting no where.\n")
            print("The lady in the sear next to you prods you and looks at you with a panicked expression.\n")
            time.sleep(2)

            choice1()

        if(choicevalue == "2"):
            print("She brushes you off.\n")
            print("Despite knowing she's only following procedure, you are getting fed up.")
            time.sleep(2)

            choice3()

def choice3():
    print("-------------------------------------------------------------------------------------------------------------***")
    time.sleep(2)
    print("You decide to find out for yourself what is going on.\n")
    time.sleep(2)
    print("You surreptitiously search the bags in the same overhead hold as you.\n")
    time.sleep(2)
    print("The fourth bag you attempt search has four padlocks on it and is extremely heavy.\n")
    time.sleep(2)
    print("You look around and there are several people now staring at you.\n")
    time.sleep(2)
    print("You hear a loud beeping.\n")
    time.sleep(2)
    print("Everything else goes quiet around you suddenly.\n")
    time.sleep(2)
    print("Sound returns like a tidal wave and you feel a momentary searing pain before you are blasted into oblivion.\n")
    time.sleep(2)
    print("Oops, YOU DIED! Shouldn't fiddle with things you don't have expertise in.\n")
    time.sleep(2)


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
            print("she orders you to sit back down.\n")
            time.sleep(2)
            print("And make sure to fasten your seatbelt as well!\n")
            time.sleep(2)
            choiceinputted = True

            choice2()

        elif(choicevalue == "3"):
            print("You decide to find out for yourself what is going on.\n")
            time.sleep(2)
            print("You surreptitiously search the bags in the same overheard locker as you.\n")
            time.sleep(2)
            choiceinputted = True

            choice3()

        else:
            print("\nYou need to choose 1, 2 or 3.\n")

main()