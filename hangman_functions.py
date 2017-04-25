import sys
import random
import time


def read_txt():
    capitals = []
    countries = []
    for line in open('countries_and_capitals.txt'):
        words = line.split("|")
        capitals.append(words[1][1:-1].upper())
        countries.append(words[0][:-1].upper())
    return capitals

def draw_capital(capitals):
    secret_capital = random.choice(capitals)  # drawn capital
    letters = list(secret_capital)  # list containing letters of the secret capital
    return secret_capital, letters

def game_status(secret_capital, count, play = "Y"):
    global end_game
    print
    if end_game == "lose":  # end of the game - if player lose all of life points
        play = input("You lost after " + str(count) + " rounds! The correct answer is " +
                     secret_capital + " Press 'Y' to play again. ").upper()
    elif end_game == "win":  # end of the game - if player guess secret capital
        play = input("You won after " + str(count) + " rounds! Press 'Y' to play again. ").upper()

    if play != "Y":  # if player presses a different button than 'Y'
        sys.exit()
    end_game = None

def  create_dashes(letters, dashes = []):
    for char in letters:
        if char is " ":
            dashes.append(" ")  # capital of two words - space between
        else:
            dashes.append("_")  # convert the capital into the dashes
    return dashes

def read_word(secret_capital):
    global life_points
    word_input = input("Enter your word: ").upper()
    if word_input == secret_capital:
        end_game = "win"  # this script run if player wins
    else:
        life_points = life_points - 2
        end_game = None
        print("You are wrong! You lose 2 life point!")

    return end_game

def read_letter(secret_capital, typped_letters, letters, life_points,dashes):
    global end_game
    letter_input = input("Enter your letter: ").upper()
    while not(letter_input.isalpha()) or len(letter_input) > 1 \
            or letter_input in typped_letters:

        if not(letter_input.isalpha()) or len(letter_input) > 1:
            letter_input = input("You have to type one " +
                                 "and only one alphabetical symbol. ").upper()
        if letter_input in typped_letters:
            print("The letter you have typped so far: ", typped_letters)
            letter_input = input("You've typped this letter already." +
                                 "Type another letter").upper()

    if letter_input in letters:
        print("You are correct!")
        typped_letters.append(letter_input)

        while letter_input in letters:
            next_index = letters.index(letter_input)
            dashes[next_index] = letter_input
            letters[next_index] = "_"
            if "".join(dashes) == secret_capital:
                end_game = "win"

    else:
        life_points = life_points - 1
        print("You are wrong! You lose 1 life point!")
        typped_letters.append(letter_input)
        end_game = None
    return life_points, end_game

def main():

    capitals = read_txt()


    print("""
        Welcome in our The Hangman Game!
        Your task is to guess the drawn capital. The capital will be displayed
        in the form of dashes. You can guess right away the whole
        word or single letter. At the beginning of the game you have 10 lives.""")
    global end_game
    end_game = None
    count = 0

    while True:

        word_input = ""  # user input - the whole word entered by user
        letter_input = ""  # user input - one letter entered by user
        life_points = 10  # player has 10 life points during one game
        user_answer = ""  # question - do you want to guess whole word or only one letter
        typped_letters = list()  # list containing letters which player typped, but this letter isn't in secret capital
        dashes = []
        
        secret_capital, letters = draw_capital(capitals)

        game_status(secret_capital, count, play = "Y")
        count = 0

        

        dashes = create_dashes(letters, dashes = [])


        while end_game == None:
            
            count += 1
            
            if len(typped_letters) > 0:
                print("Letters you have typped so far: ", typped_letters)
            print("".join(dashes), "\n")


            user_answer = input("You have " + str(life_points) + " life points!" +
                                " If you want to guess a whole word press 'W' " +
                                "or a letter press 'L' ").upper()

            if user_answer == "W":

                end_game = read_word(secret_capital)

            elif user_answer == "L":  # this block run when player wants to guess
                                        # a letter
                life_points, end_game = read_letter(secret_capital, typped_letters, letters, life_points, dashes)

            if life_points == 0:
                end_game = "lose"

if __name__ == '__main__':
    main()