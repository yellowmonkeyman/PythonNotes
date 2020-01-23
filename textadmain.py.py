
#A FUNCTION FOR EACH OF THE CHOICES AND THEIR OPTIONS

def choice_1_1():

    choiceinputted2 = False

    while(choiceinputted2 == False):
        choicevalue2 = input("Enter your choice: ")

        if(choicevalue2 == "1"):
            print("\nAs you approach the stewardesses, you hear the word 'terrorist'")
            print("however they simply ask you to go back to your seat.\n")
            print("What do you do next?\n")
            choiceinputted2 = True

            
        elif(choicevalue2 == "2"):
            print("\nThe person next to you shrugs you off.\n")
            choiceinputted2 = True

        elif(choicevalue2 == "3"):
            print("\nThe stewardesses go into the cockpit.")
            print("Your hear the crackling of the plane's anouncement system")
            print("'Greetings Ladies and Gentleman, we will be performing a routine bag inspection\n")
            choiceinputted2 = True

        else:
            print("You need to choose 1, 2 or 3.")


def main():

    print("\n1/ Ask Stewardesses\n")
    print("2/ Ask the person next to you\n")
    print("3/ Do nothing and see what happens\n")

    choiceinputted1 = False

    while(choiceinputted1 == False):
        choicevalue1 = input("Enter your choice: ")

        if(choicevalue1 == "1"):
            print("\nAs you approach the stewardesses, you hear the word 'terrorist'")
            print("however they simply ask you to go back to your seat.\n")
            print("\nThe stewardesses go into the cockpit.")
            print("You hear the crackling of the plane's anouncement system")
            print("'Greetings Ladies and Gentleman, we will be performing a routine bag inspection\n")
            print("What do you do next?\n")
            choiceinputted1 = True

            choice_1_1()

            
        elif(choicevalue1 == "2"):
            print("\nThe person next to you shrugs you off.\n")
            print("\nThe stewardesses go into the cockpit.")
            print("You hear the crackling of the plane's anouncement system")
            print("'Greetings Ladies and Gentleman, we will be performing a routine bag inspection\n")
            choiceinputted1 = True

            choice_1_1()

        elif(choicevalue1 == "3"):
            print("\nThe stewardesses go into the cockpit.")
            print("You hear the crackling of the plane's anouncement system")
            print("'Greetings Ladies and Gentleman, we will be performing a routine bag inspection\n")
            choiceinputted1 = True

            choice_1_1()

        else:
            print("You need to choose 1, 2 or 3.")

main()
