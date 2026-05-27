#Dog breeds practice CREATE
#Purpose: Recommend a dog breed to users depending on their needs

#Init
import pandas as pd
import webbrowser
data=pd.read_csv('dog.csv')
print(data)

min_weight=data["Minimum Weight"].tolist()
name=data["Name"].tolist()
temp=data["Temperament"].tolist()
image=data["Image"].tolist()
bred_for=data["BredFor"].tolist()

filter=[]

#Functions
def getDogSize(size):
    for i in range(len(min_weight)):
        if size=="Tiny" and min_weight[i]<=10:
            filter.append(name[i])
        elif size=="Small" and min_weight[i]>=11 and min_weight[i]<=25:
            filter.append(name[i])
        elif size=="Medium" and min_weight[i]>=26 and min_weight[i]<=60:
            filter.append(name[i])
        elif size=="Large" and min_weight[i]>60:
            filter.append(name[i])
    print(filter)
    filter.clear()

def search(breed_name):
    for i in range(len(name)):
        if breed_name in name[i]:
            filter.append(temp[i])
            print(filter)
            filter.clear()
            filter.append(image[i])
            webbrowser.open(image[i])
            filter.clear()

def breeding(purpose):
        for i in range(len(bred_for)):
            if purpose in bred_for[i]:
                filter.append(name[i])
        if filter==[]:
            print("No Matching Breed - Try Again")
        print(filter)
        filter.clear()

def menu():
    while True:
        choice=input("""What would you like to search for to find your perfect dog?
                    1. Search Dog Size
                    2. Search a Specific Dog Breed
                    3. Search the Purpose of a Dog
                    -> """)
        if choice=="1":
            size_choice=input("""What size dog are you looking for?
                            1. Tiny
                            2. Small
                            3. Medium
                            4. Large
                            -> """).capitalize()
            getDogSize(size_choice)
        elif choice=="2":
            breed_choice=input("What dog breed are you looking for?: ") 
            search(breed_choice)
        elif choice=="3":
            purpose_choice=input("What purpose do you want your dog to have?: ").capitalize()
            breeding(purpose_choice)
        cont=input("Would you like to continue searching? (Y/N): ").capitalize()
        if cont=="Y":
            continue
        elif cont=="N":
            print("Hope you find your dream dog!")
            break


#Main
menu()


#Dataset Source Information:
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
