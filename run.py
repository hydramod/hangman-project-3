import random
import os
import nltk
from nltk.corpus import wordnet
import gspread
from google.oauth2.service_account import Credentials

#download words and definitions from nltk corpus
nltk.download('wordnet')
english_words = list(wordnet.words())

SCOPE = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = CLIENT.open('Hangman')
LEADERBOARD = SHEET.worksheet('Leaderboard')

#function to print the title
def title():
    print("\033[33m888                                                            ")
    print("888                                                            ")
    print("888                                                            ")
    print("88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  ")
    print("888 \"88b    \"88b888 \"88bd88P\"88b888 \"888 \"88b    \"88b888 \"88b ")
    print("888  888.d888888888  888888  888888  888  888.d888888888  888 ")
    print("888  888888  888888  888Y88b 888888  888  888888  888888  888 ")
    print("888  888\"Y888888888  888 \"Y88888888  888  888\"Y888888888  888 ")
    print("                             888                              ")
    print("                        Y8b d88P                              ")
    print("                         \"Y88P\"                               \033[0m")
    print("\n")

# function to select difficulty level
def select_difficulty_level():
    # Prints a menu of difficulty levels.
    print("Select difficulty level:")
    print("1. \033[97mEasy\033[0m")
    print("2. \033[33mMedium\033[0m")
    print("3. \033[38;5;208mHard\033[0m")
    print("4. \033[31mExpert\033[0m")
    level = int(input("Enter your choice (1-4): "))
    #os.system('clear')
    # Depending on the user's choice of difficulty level, sets the number of hint calls allowed and the number of guesses.
    if level == 1:
        hint_calls_allowed = 2
        return 5, hint_calls_allowed
    elif level == 2:
        hint_calls_allowed = 2
        return 10, hint_calls_allowed
    elif level == 3:
        hint_calls_allowed = 4
        return 15, hint_calls_allowed
    elif level == 4:
        hint_calls_allowed = 8
        return 45, hint_calls_allowed
    else:
        # If the user enters an invalid choice, prints an error message and returns None for both values.
        print("\033[31mInvalid input. Please try again.\033[0m")
        return None, None

# function to choose a random word
def get_word(max_length):
    # initialize an empty string
    word = ""
    # keep looping until a valid word is generated
    while not word.isalpha() or len(word) > max_length:
        # choose a random word from a list of English words
        word = random.choice(english_words)
    # return the word in uppercase
    return word.upper()

# function to play the game
def play():
    # initialize the flag for playing again
    play_again = True
    # loop until the user chooses to stop playing
    while play_again:
        # select the difficulty level and get the max length of the word and the number of hint calls allowed
        max_length, hint_calls_allowed = select_difficulty_level()
        # if the user entered an invalid input, continue the loop
        if max_length is None or hint_calls_allowed is None:
            continue
        # get a random word from the list of English words with length <= max_length and convert 
        word = get_word(max_length)
        # create a string with "" as placeholders for the letters of the word
        word_completion = "_" * len(word)
        # initialize the guessed flag to False, and empty lists for guessed letters and guessed words
        guessed = False
        guessed_letters = []
        guessed_words = []
        # set the number of tries to 6
        tries = 6
        # print the starting message, the current hangman display, word length and number of hints
        #os.system('clear')
        print("Let's play Hangman!")
        print("Letters: " + str(len(word)))
        print("Type # for a hint, you have",hint_calls_allowed,"left!" )
        print(display_hangman(tries))
        # print the current state of the word (with "" placeholders)
        print(word_completion)
        print("\n")
        # loop until the user guesses the word or runs out of tries
        while not guessed and tries > 0:
            try:
                # get a guess from the user (either a letter or a word)
                guess = input("Please guess a letter or word: ").upper()
            except StopIteration:
                # if the user cancels the game (e.g., by pressing Ctrl+C), exit the loop and return from the function
                return
            # if the user wants a hint, and there are hints remaining, call the hint function and continue the loop
            if guess == "#":
                if hint_calls_allowed > 0:
                    hint(word)
                    hint_calls_allowed -= 1
                else:
                    print("\033[31mSorry, no hints remaining.\033[0m")
                continue
            # if the guess is a single letter
            if len(guess) == 1 and guess.isalpha():
                # if the letter was already guessed, print a message and continue the loop
                if guess in guessed_letters:
                    print("\033[36mYou already guessed the letter", guess,"\033[0m")
                    # if the letter is not in the word, decrement the number of tries and add the letter to the list of guessed letters
                elif guess not in word:
                    print("\033[31m" + guess + " is not in the word." + "\033[0m")
                    tries -= 1
                    guessed_letters.append(guess)
                    # if the letter is in the word, update the word_completion string with the guessed letter
                else:
                    print("\033[32mGood job,", guess, "is in the word!\033[0m")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    # if there are no more "" placeholders in the word_completion string, set the guessed flag to True
                    if "_" not in word_completion:
                        guessed = True
            # if the guess is a word of the same length as the target word
            elif len(guess) == len(word) and guess.isalpha():
                # if the word was already guessed, print a message and continue the loop
                if guess in guessed_words:
                    print("\033[36mYou already guessed the word", guess,"\033[0m")
                elif guess != word:
                    # If the player guessed the wrong word, decrement the number of tries left, 
                    # and append the guessed word to the list of guessed words.
                    print("\033[91m" + guess + " is not the word." + "\033[0m")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    # If the player guessed the correct word, set guessed to True and 
                    # set the word completion to the correct word.
                    guessed = True
                    word_completion = word
            else:
                # If the guess is not a valid guess
                print("Not a valid guess.")
            # Print the current state of the hangman and the word completion.
            print(display_hangman(tries))
            print("\033[32m" + word_completion + "\033[0m")
            print("\n")
        if guessed:
            # If the player has guessed the word
            print("\033[33mCongratulations, you guessed the word! You win!\033[0m")
            add_score(word)
        else:
            # If the player has run out of tries
            print("\033[31mSorry, you ran out of tries. The word was " + word + ".\033[0m")
        # Get input from the player to see if they want to play again.
        play_again = play_again_input()
        #os.system('clear') 
    # Print a message to thank the player for playing.
    print("Thanks for playing Hangman!")

#function to handle hints
def hint(word):
    #get the synset (set of synonyms) for the word
    synset = wordnet.synsets(word)
    #if the synset exists
    if synset:
        #get the definition of the first synset
        definition = synset[0].definition()
        print("Definition:", definition)
    else:
        print("Sorry, no definition found for this word.")
    #get a random index within the range of the word length
    random_index = random.randint(0, len(word)-1)
    #print the character at the random index in the word
    print("Random letter in the word:", word[random_index])

#function to prompt user to play again
def play_again_input():
    #get user input to play again
    play_again_input = input("Would you like to play again? (Y/N)").upper()
    #while the input is not Y or N
    while play_again_input != 'Y' and play_again_input != 'N':
        #prompt the user to enter either Y or N
        play_again_input = input("Please enter either Y or N.").upper()
    #return True if the input is Y, False if it is N
    return play_again_input == 'Y'

# function to display the hangman
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
            ]
    return stages[tries]

# function to load scores from Google Sheets
def load_scores():
    # retrieve all records from Google Sheets
    scores = LEADERBOARD.get_all_records()
    return scores

# function to save scores to Google Sheets
def save_scores(scores):
    # clear all existing records in the Google Sheets
    LEADERBOARD.clear()
    # insert header row at the top of the sheet
    LEADERBOARD.insert_row(['Rank', 'Name', 'Score'], 1)
    # loop through each score and insert it as a new row in the Google Sheets
    for i, score in enumerate(scores, start=2):  
        LEADERBOARD.insert_row([i - 1, score['Name'], score['Score']], i)

# Function to add score to leaderboard
def add_score(word):
    # Get player name and score
    name = input("Enter your name: ")
    score = len(word)
    # Load leaderboard scores
    scores = load_scores()
    # Flag to check if player already exists
    found_player = False
    # Iterate through scores to check if player already exists
    for s in scores:
        if s['Name'].lower() == name.lower():
            found_player = True
            # If player exists, add points to existing score
            s['Score'] += score
            save_scores(scores)
            print(f"Added {score} points to {name}. New score: {s['Score']}")
            break
    # If player is not found, add new score to leaderboard
    if not found_player:
        new_score = {'Name': name, 'Score': score}
        scores.append(new_score)
        scores = sorted(scores, key=lambda k: int(k['Score']), reverse=True)
        save_scores(scores)
        print(f"Added score: {name} - {score}")

# View the leaderboard
def view_leaderboard():
    # Load the scores from the file
    scores = load_scores()
    # If there are no scores, inform the user
    if len(scores) == 0:
        print("No scores found.")
    else:
        # Print the leaderboard header
        print("Rank\tName\tScore")
        # Loop through the scores and print each one
        for i, score in enumerate(scores, start=1):
            print(f"{i}\t{score['Name']}\t{score['Score']}")

# Delete a score
def delete_score():
    # Get the name of the player to delete
    name = input("Enter the name of the player to delete: ")
    # Load the scores from the file
    scores = load_scores()
    # Create a new list of scores without the specified player
    updated_scores = [score for score in scores if name.lower() not in score['Name'].lower()]
    # If the length of the updated list is the same as the original, the player was not found
    if len(updated_scores) == len(scores):
        print(f"No player with name '{name}' found.")
    else:
        # Save the updated scores to the file
        save_scores(updated_scores)
        # Inform the user that the player was deleted
        print(f"Deleted player: {name}")

# Display the leaderboard menu
def leaderboard_menu():
    while True:
        # Display the menu options
        print("\nPick an option:")
        print("1. View leaderboard")
        print("2. Delete a score")
        print("3. Main Menu")
        # Get the user's choice
        choice = input("Enter your choice (1-3): ")
        # Process the user's choice
        if choice == '1':
            # Clear the screen and display the leaderboard
            #os.system('clear')
            view_leaderboard()
        elif choice == '2':
            # Clear the screen and delete a score
            #os.system('clear')
            delete_score()
        elif choice == '3':
            # Return to the main menu
            main()            
            break
        else:
            # Inform the user of an invalid choice
            print("Invalid choice. Please enter a number between 1 and 3.") 

# Main function to start the game
def main():
    # Display the title screen
    title()
    while True: 
        # Display the main menu options
        print("\nPick an option:")
        print("1. Start a new game")
        print("2. Leaderboard")
        print("3. Quit")

        # Get the user's choice
        choice = input("Enter your choice (1-3): ")

        # Process the user's choice
        if choice == '1':
            # Clear the screen and start a new game
            #os.system('clear')
            play()
        elif choice == '2':
            # Clear the screen and display the leaderboard menu
            #os.system('clear')
            leaderboard_menu()
        elif choice == '3':
            # Quit the game
            print("Exiting...")
            break
        else:
            # Inform the user of an invalid choice
            print("Invalid choice. Please enter a number between 1 and 3.")

# call the main function
if __name__ == "__main__":
    main()
