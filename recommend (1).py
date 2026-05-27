#Leila
#Recommend an image

#Init
import webbrowser

#Functions
def recommend():
    print("Welcome to the Movie Recommender, where I recommend you movies based on your responses")
    genre=input("""First question: What is your preferred movie genre?
                1. Romance
                2. Comedy
                3. Horror
                4. Action
                --> """)
    if genre=="1": #Prints and opens the image and description best fit to the users input
        webbrowser.open(url[0])
        print(description[0])

    elif genre=="2":
        webbrowser.open(url[1])
        print(description[1])

    elif genre=="3":
        webbrowser.open(url[2])
        print(description[2])

    elif genre=="4":
        webbrowser.open(url[3])
        print(description[3])

#Main
url=["file:///C:/Users/ljusufovic/Pictures/Shirt_Choice.jpg", #10 Things I Hate About You
     "https://tinyurl.com/3fsusfzz", #White Chicks
     "https://tinyurl.com/39cvteuy", #The Shining
     "https://tinyurl.com/y755h24p" #The Dark Knight
     ] #Image links

description=["10 Things I Hate About You is a classic romance movie for the classic romance movie lover. This movie is good for people interested in following a high school romance story with elements of angst",
             "White Chicks is a hilarious comedy movie following two men cosplaying as women while trying to navigate the world and fit in through their new identities. This movie is definitely cry-laugh worthy",
             "The Shining is a horror movie adapted from the famous horror novel by the one and only Stephen King. This movie involves elements of suspense, paranormal activity, and lip-quivering moments",
             "The Dark Knight is an action packed movie following Batman and his conquest to defeat supervillains the Joker and Two-Face while trying to save the city of Gotham. This movie is good for people looking for many suspenseful fight scenes, which are geniously directed by Christopher Nolan"]
            #Descriptions best fit for each movie

recommend()
#Source Info

#1:
#Website name: sceneandheardnu.com
#URL: https://www.sceneandheardnu.com/content/2023/7/3/an-ode-to-10-things-i-hate-about-you
#Author name: Julia Catrambone
#Date: July 3, 2023
#Name of article: An Ode to "10 Things I Hate About You"

#2:
#Website name: nytimes.com
#URL: https://www.nytimes.com/2024/06/25/movies/white-chicks-anniversary.html
#Author name: Robert Daniels
#Date: June 25, 2024
#Name of article: ‘White Chicks’ at 20: Comedy Beyond the Pale

#3
#Website name: people.com
#URL: https://people.com/movies/the-shining-twins-now-naturally-spooky/
#Author name: Alexia Fernandez
#Date: October 25, 2022
#Name of article: See 'The Shining' Twins Now: The Iconic Pair Say They Are 'Naturally Spooky'

#4:
#Website name: projectedfigures.com
#URL: https://projectedfigures.com/2016/03/24/the-dark-knight-2008/
#Author name: rantbit
#Date: March 24, 2016
#Name of article: The Dark Knight (2008)
