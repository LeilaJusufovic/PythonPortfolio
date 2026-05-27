#Leila
#Nickname generator
def nickname():
    while True:
        print("Welcome to your nickname generator! Please choose whichever option you like best!")
        time=input("Do you prefer daytime or nighttime?: ").capitalize()
        #Daytime generator
        if time=="Daytime":
            color=input("Do you prefer pink or blue?: ").capitalize()
            if color=="Pink":
                food=input("Do you prefer candy or chocolate?: ").capitalize()
                if food=="Candy":
                    print("Your name is Sunny Cotton Candy!")
                if food=="Chocolate":
                    print("Your name is Sweet Bright Rose!")
            if color=="Blue":
                food=input("Do you prefer chips or popcorn?: ").capitalize()
                if food=="Chips":
                    print("Your name is Crunchy Sky!")
                if food=="Popcorn":
                    print("Your name is Fluffy Cloud!")
        #Nighttime generator
        elif time=="Nighttime":
            color=input("Do you prefer black or blue?: ").capitalize()
            if color=="Black":
                food=input("Do you prefer strawberry or banana?: ").capitalize()
                if food=="Strawberry":
                    print("Your name is Juicy Red Star!")
                if food=="Banana":
                    print("Your name is Soft Night Moon!")
            if color=="White":
                food=input("Do you prefer coffee or tea?: ").capitalize()
                if food=="Coffee":
                    print("Your name is Energizer Alien!")
                if food=="Tea":
                    print("Your name is Pure Earl Planet!")
        #Continue
        else:
            print("Please put 1 of 2 options!")
        user_input=input("Would you like to restart? (Yes or No)?: ").capitalize()
        if user_input=="Yes":
            print("Restarting now . . .")
        if user_input=="No":
            print("Thanks for playing!")
            break

nickname()
