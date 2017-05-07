import csv
import random
import sys
from datetime import datetime
import time

def music_option():
    
    music_file = open('music1.csv', 'r') #"r" - to read .csv file
    reader = csv.reader(music_file, delimiter = "|") #delimiter - Splits columns into a file
    col_list = list(reader) #col_list - Each line in this list is a separate list


    collector_list = [] #The main list in my program

    for pre_collector_list in col_list:  
        collector_list.append([(pre_collector_list[0].strip(), pre_collector_list[1].strip()),
        (pre_collector_list[2].strip(), pre_collector_list[3].strip(), pre_collector_list[4].strip())])
    return collector_list  #Each line of the .csv file is a separate list consisting of two tuples: 
                            #first - artist and album, second - year of publication, genre and length.
                            #() - create a tuple inside of list
                            #append - Adds items to the collector_list
                            #strip() - Removes whitespace
def change_to_sec(time_str):
    m, s = time_str.split(':')
    change_sec = int(m) * 60 + int(s)
    return change_sec


def  choice():  #This function returns a user input
    user_choice =  ""
    user_options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    while not user_choice in user_options:
        user_choice = input("""
        Welcome in the CoolMusic! Choose the action:

        1) Add new album
        2) Find albums by artist
        3) Find albums by year
        4) Find musician by album
        5) Find albums by letter(s)
        6) Find albums by genre
        7) Calculate the age of all albums
        8) Choose a random album by genre
        9) Show the amount of albums by an artist
        10) Find the longest-time album
        0) Exit\n""")   #"\n" - add enter to for better readability
       
    return user_choice

def logic(collector_list, user_choice):
    #This function as arguments accepts the collector list to know what it is and user input to decide what to do next
    while True:
        if user_choice == "1": #add new album
            add_artist = input("Enter the name of the artist: ").upper()
            add_album = input("Enter the name of the album: ").upper()
            add_year = input("Enter a year of release: ").upper()
            add_gentre = input("Enter the music genre of the album: ").upper()
            add_length = input("Enter the length of the album: ").upper()

            music_file= open("music1.csv", "a") #"a" - append - add new line in .csv file
            music_file.write(add_artist + "," + add_album + "," + add_year + "," + add_gentre + "," + add_length)
            music_file.close()
            break

        if user_choice == "2": # find album by artist
            choice_artist = input("Enter the artist whose album you want to find: ").title()
                                                    #The method title() returns 
                                                    #a copy of the string in which first 
                                                    #characters of all the words are capitalized.
            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if choice_artist == pre_collector_list[0][0]:
                    print("\n" + "ARTIST: "+ pre_collector_list[0][0])
                    print("\n" + "ALBUM: " + pre_collector_list[0][1])
                    print("\n" + "YEAR: " + pre_collector_list[1][0])
                    print("\n" + "GENRE: " + pre_collector_list[1][1])
                    print("\n" + "LENGTH: " + pre_collector_list[1][2] + "\n")
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such artist. Try again!")
                break     
        

        if user_choice == "3": #Find albums by year
            choice_year = input("Enter the year of release of the album you want to find: ")
            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if choice_year == pre_collector_list[1][0]:
                    print("\n" + "ARTIST: "+ pre_collector_list[0][0])
                    print("\n" + "ALBUM: " + pre_collector_list[0][1])
                    print("\n" + "YEAR: " + pre_collector_list[1][0])
                    print("\n" + "GENRE: " + pre_collector_list[1][1])
                    print("\n" + "LENGTH: " + pre_collector_list[1][2] + "\n")
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such year. Try again!")
                break    
    
        
        if user_choice == "4": #Find musician by album
            choice_album = input("Enter the album whose artist you want to find: ").title() #The method title() returns 
                                                                                            #a copy of the string in which first 
                                                                                            #characters of all the words are capitalized.
            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if choice_album == pre_collector_list[0][1]:
                    print("\n" + "ARTIST: "+ pre_collector_list[0][0])
                    print("\n" + "ALBUM: " + pre_collector_list[0][1])
                    print("\n" + "YEAR: " + pre_collector_list[1][0])
                    print("\n" + "GENRE: " + pre_collector_list[1][1])
                    print("\n" + "LENGTH: " + pre_collector_list[1][2] + "\n")
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such album. Try again!" + "\n")
                break    
        
        if user_choice == "5": #Find albums by letter(s)
            choice_letter = input(("Enter a letter: ")).lower() #The method lower() returns a copy of the string 
                                                                #in which all case-based characters have been lowercased.
            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if any(choice_letter in s for s in pre_collector_list[0][1]):
                    matching = [s for s in pre_collector_list[0][1] if choice_letter in s]

                    print("\n" + "ARTIST: "+ pre_collector_list[0][0])
                    print("\n" + "ALBUM: " + pre_collector_list[0][1])
                    print("\n" + "YEAR: " + pre_collector_list[1][0])
                    print("\n" + "GENRE: " + pre_collector_list[1][1])
                    print("\n" + "LENGTH: " + pre_collector_list[1][2] + "\n")
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such letter. Try again!")
                break    
        
        if user_choice == "6": #Find albums by genre
            choice_genre = input("Enter the genre you want to find: ").lower() #The method lower() returns a copy of the string 
                                                                             #in which all case-based characters have been lowercased.
            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if choice_genre == pre_collector_list[1][1]:
                    print("\n" + "ARTIST: "+ pre_collector_list[0][0])
                    print("\n" + "ALBUM: " + pre_collector_list[0][1])
                    print("\n" + "YEAR: " + pre_collector_list[1][0])
                    print("\n" + "GENRE: " + pre_collector_list[1][1])
                    print("\n" + "LENGTH: " + pre_collector_list[1][2] + "\n")
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such genre. Try again!")
                break    
        
        if user_choice == "7": #Calculate the age of all albums
            for pre_collector_list in collector_list:
                albums_age = 2017 - int(pre_collector_list[1][0])
                print(pre_collector_list[0][1] + ", whose artist is " +  pre_collector_list[0][0] + ", is " + str(albums_age) + " years old!" + "\n")
            break

        if user_choice == "8": #Choose a random album by genre
            choice_genre_random = input("Enter a genre: ").lower() #The method lower() returns a copy of the string 
                                                                      #in which all case-based characters have been lowercased.
                                                               
            album_by_genre_list = [] #create an empty list, later list of albums of chosen genre

            for pre_collector_list in collector_list:
                if choice_genre_random == pre_collector_list[1][1]: #If choice_genre_random is equal to the second element of the second tuple(genre)
                    album_by_genre_list.append(pre_collector_list[0][1]) #add to list second element of first tuple (album)

            random_album = random.choice(album_by_genre_list) #find randomly album from album_by_genre_list
                                                            #random.choice - return a random element from the non-empty sequence

            for pre_collector_list in collector_list:
                if random_album == pre_collector_list[0][1]: #is equal to album on the list
                    print("\n" + "My music collector can offer you " + random_album + " whose artist is " + pre_collector_list[0][0] + "!")
            break
        
        if user_choice == "9": #Show the amount of albums by an artist
            choice_artist_amound = input("Enter the artist whose amount of albums you want to see: ").title()
            albums_amound = [] 

            count = 0 #After leaving the for loop, this variable is zeroed
            for pre_collector_list in collector_list:
                if choice_artist_amound == pre_collector_list[0][0]: # user inputis equal to artist on pre_collector list
                    albums_amound.append(pre_collector_list[0][1]) ##add to albums_amound list second element of first tuple (album)
                    amound = str(len(albums_amound)) #Show list length, replace it to string; list length is equal to amound of albums of this artist
                    #amound = pre_collector_list[0][1].count(pre_collector_list[0][1])
                    count = count + 1 #After each loop if passes - 1 is added, To search another line - enter to the loop again
            if count > 0: #Found the input match, interrupts, exits the loop if and come back to while True loop
                print("\n" + "The music collector contains ", amound,   " album(s) of this artist!")
                break

            if count == 0: #No input match found, interrupt, exit loop to while True loop
                print("\n" + "Collector doesn't have such artist. Try again!")
                break

        if user_choice == "10": #Find the longest-time album
            biggest = [] #empty list, later list of timing in sec
            for pre_collector_list in collector_list:
                biggest.append(change_to_sec(pre_collector_list[1][2]))
                maxi = max(biggest) #the longest album in sec
            print("The longest album in my music collector lasts" , maxi, " seconds!")
            break

        if user_choice == "0":
            print("Thank you for use my music collector!")
            sys.exit() 
            

def main(): #contain everything
    collector_list = music_option() #to make music collector only once

    while True: #With this loop, it will be able to select a new option and continue to update the user input
        user_choice = choice() #To the variable user_choice assigns what is returned from the choice function, which is user input
        logic(collector_list, user_choice) #Shows collector_list- to know what it is and user_choice to know what to do next

if __name__ == '__main__': 
    main() #turn on functions