import time

def TitlePage():
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

MAX_QUESTION = 3200
PLAYER_WON = 3201
PLAYER_LOST = 3202

PLAYER_LOST=0

Prompt = [
           ["You awake in your plane seat.","You're confused but notice two stewardesses several rows in front.","They appear extremely concerned and distrought.","What do you do?", "1. End Game"]
         ]
Answers = [[PLAYER_WON]]

def GetPrompt(n):
    s="\n"
    for part in Prompt[n]:
        s += part
        s += "\n"
    return s

def GetPositiveInt(prompt):
    # choice is the numeric option entered by the user
    choice = -1
    while choice < 0:
        # Get a string from the user
        choiceString = input(prompt)
        # Validate that the string is numeric
        valid = True
        for s in choiceString:
            if  not(s.isdigit()):
                valid = False
        if not(valid):
            # Output an error message
            print("That is not a valid number, try again!")
        else:
            # Convert the string to an integer
            choice = int(choiceString)
    # Return the integer choice entered by the user
    return choice


def GetChoice(n):
    choice = -1
    prompt = "Enter choice [1-" + str(len(Answers[n])) + "] >"
    while choice < 0:
        choice = GetPositiveInt(prompt)
        if choice < 1 or choice > len(Answers[n]):
            print("Invalid choice, try again")
            choice = -1
    # Return positive integer 1 to len(Answers[n])
    return choice

def MainGameLoop():
    question = 0

    while question < MAX_QUESTION:
        print(GetPrompt(question))

        choice = GetChoice(question)
        question = Answers[question][choice - 1]

    return question == PLAYER_WON

def PlayerWon():
    print("\nCongratulations, you won\n")

def PlayerLost():
    print("\nLoser!\n")

def main():

    TitlePage()
    if MainGameLoop():
        PlayerWon()
    else:
        PlayerLost()

main()