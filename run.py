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
    print("Select difficulty level:")
    print("1. \033[97mEasy\033[0m")
    print("2. \033[33mMedium\033[0m")
    print("3. \033[38;5;208mHard\033[0m")
    print("4. \033[31mExpert\033[0m")
    level = int(input("Enter your choice (1-4): "))
    if level == 1:
        hint_calls_allowed = 1
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
        print("\033[31mInvalid input. Please try again.\033[0m")
        return None, None

# function to choose a random word
def get_word(max_length):
    word = ""
    while not word.isalpha() or len(word) > max_length:
        word = random.choice(english_words)
    return word.upper()

# function to play the game
def play():
    play_again = True
    while play_again:
        max_length, hint_calls_allowed = select_difficulty_level()
        if max_length is None or hint_calls_allowed is None:
            continue
        word = get_word(max_length)
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            try:
                guess = input("Please guess a letter or word: ").upper()
            except StopIteration:
                return
            if guess == "HINT":
                if hint_calls_allowed > 0:
                    hint(word)
                    hint_calls_allowed -= 1
                else:
                    print("\033[31mSorry, no hints remaining.\033[0m")
                continue
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("\033[36mYou already guessed the letter", guess,"\033[0m")
                elif guess not in word:
                    print("\033[31m" + guess + " is not in the word." + "\033[0m")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("\033[32mGood job,", guess, "is in the word!\033[0m")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("\033[36mYou already guessed the word", guess,"\033[0m")
                elif guess != word:
                    print("\033[91m" + guess + " is not the word." + "\033[0m")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(display_hangman(tries))
            print("\033[32m" + word_completion + "\033[0m")
            print("\n")
        if guessed:
            print("\033[33mCongratulations, you guessed the word! You win!\033[0m")
        else:
            print("\033[31mSorry, you ran out of tries. The word was " + word + ".\033[0m")
        play_again = play_again_input()
    print("Thanks for playing Hangman!")

#function to handle hints
def hint(word):
    synset = wordnet.synsets(word)
    if synset:
        definition = synset[0].definition()
        print("Definition:", definition)
    else:
        print("Sorry, no definition found for this word.")
    random_index = random.randint(0, len(word)-1)
    print("Random letter in the word:", word[random_index])

#function to prompt user to play again
def play_again_input():
    play_again_input = input("Would you like to play again? (Y/N)").upper()
    while play_again_input != 'Y' and play_again_input != 'N':
        play_again_input = input("Please enter either Y or N.").upper()
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
