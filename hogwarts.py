#leila
#assign a hogwarts house
import time
import random

def main():
    while True:
        print("Welcome to Hogwarts! Please Step Under the Sorting Hat!")
        name=input("Please enter your first name: ").capitalize()
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print(house(name))
        user_input=input("Would you like to change houses? (Yes or No)?: ").capitalize()
        if user_input=="Yes":
            print("Restarting now . . .")
        if user_input=="No":
            print("Enjoy your time at Hogwarts!")
            break

#determine house
def house(name):
        if name=="Harry" or name=="Hermione" or name=="Ron" or name=="Ginny" or name=="Fred" or name=="George":
            return "Gryffindor"
        if name=="Draco" or name=="Voldemort" or name=="Tom" or name=="Blaise" or name=="Lucius" or name=="Bellatrix":
            return "Slytherin"
        if name=="Cho":
            return "Ravenclaw"
        if name=="Cedric":
            return "Hufflepuff"
        else:
            x=random.randint(1,4)
            if x==1:
                return "Gryffindor"
            if x==2:
                return "Slytherin"
            if x==3:
                return "Ravenclaw"
            if x==4:
                return "Slytherin"
main()
