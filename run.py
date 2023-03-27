import random
import nltk
from nltk.corpus import wordnet

#download words and definitions from nltk corpus
nltk.download('wordnet')
english_words = list(wordnet.words())

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
        # print the starting message and the current hangman display
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
        else:
            # If the player has run out of tries
            print("\033[31mSorry, you ran out of tries. The word was " + word + ".\033[0m")
        # Get input from the player to see if they want to play again.
        play_again = play_again_input()
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

# main function to start the game
def main():
    title()
    play()

# call the main function
if __name__ == "__main__":
    main()
