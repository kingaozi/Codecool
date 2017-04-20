import sys

dictionary = {} #empty dictionary

def choose_option():
    
    dictionary_file = open("dictionary.CSV", "r")  #read .csv file

    for line in dictionary_file:
        dictionary_list = line.split(" | ") #split line by using " | "
        appellation = dictionary_list[0] #appellation has 0 index on the list

        definition_source = tuple(dictionary_list[1][:-1].split("_")) #making tuple which contain definition + source
        dictionary[appellation] = definition_source

    dictionary_file.close()  #exit the .csv file

    user_options = ["0", "1", "2", "3"] #options for user input
    
    global user_choice #define user_choice for whole program
    user_choice = "" #define user_choice like a string
                                                                #The program works as long as the user gives numbers from 0 to 3
    while not user_choice in user_options: #triple quotation -  the literall can span through multiple lines
        user_choice = input("""     
Dictionary for a little programer:
1) search explanation by appellation
2) add new definition
3) show all appellations alphabetically
0) exit\n""") 

choose_option()

while not user_choice == 0: #The program works until the user enters 0
    
    if user_choice == "1": #search explanation by appellation
        choice_appellation = input("Enter the appellation you chose: ")
        choice_appellation = choice_appellation.lower() #user input lowercase

        if choice_appellation in dictionary: #check if user input in dictionary
            print("\n" + choice_appellation.upper() + ": " + (dictionary[choice_appellation][0]))
            print("\n" + "Source: " + (dictionary[choice_appellation][1]))
            choose_option()
        else:
            print("Dictionary does not have such appellation. Try again.")
            choose_option()
    
    elif user_choice == "2": #add new definition
        add_appellation = input("Enter the appellation you want to add: ").lower() #user input lowercase
        add_definition = input("Enter the definition of the appellation you chose: ").lower()
        add_source = input("Enter the source of the definition you chose: ").lower()
        dictionary_file = open("dictionary.CSV", "a") #append to the .csv file
        dictionary_file.write(add_appellation + " | " + add_definition + "_" + add_source + "\n")
        dictionary_file.close() #exit from .csv file
        choose_option()

    elif user_choice == "3": #show all appellations alphabetically
        no = 1 #View appellations in numeric order
        for key in sorted(dictionary.keys()):
            print(str(no) + ")" + key) #separate numbers with appellation by ")"
            no += 1 #add 1 to previous number
        choose_option()
    
    if user_choice == "0": #exit
        print("Thank you for using my dictionary. See you later")
        sys.exit() #exit from program


            
    