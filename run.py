import random
import nltk
from nltk.corpus import words

#download words from nltk corpus
nltk.download('words')
english_words = words.words()

# function to choose a random word
def get_word():
    word = ""
    while not word.isalpha():
        word = random.choice(english_words)
    return word.upper()

# function to play the game
def play():
    play_again = True
    while play_again:
        word = get_word()
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("888                                                            ")
        print("888                                                            ")
        print("888                                                            ")
        print("88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  ")
        print("888 \"88b    \"88b888 \"88bd88P\"88b888 \"888 \"88b    \"88b888 \"88b ")
        print("888  888.d888888888  888888  888888  888  888.d888888888  888 ")
        print("888  888888  888888  888Y88b 888888  888  888888  888888  888 ")
        print("888  888\"Y888888888  888 \"Y88888888  888  888\"Y888888888  888 ")
        print("                             888                              ")
        print("                        Y8b d88P                              ")
        print("                         \"Y88P\"                               ")
        print("\n")
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            try:
                guess = input("Please guess a letter or word: ").upper()
            except StopIteration:
                return
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
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
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Congratulations, you guessed the word! You win!")
            play_again_input = input("Would you like to play again? (Y/N)").upper()
            while play_again_input != 'Y' and play_again_input != 'N':
                play_again_input = input("Please enter either Y or N.").upper()
            if play_again_input == 'Y':
                play_again = True
            else:
                play_again = False
        else:
            print("Sorry, you ran out of tries. The word was " + word + ".")
            play_again_input = input("Would you like to play again? (Y/N)").upper()
            while play_again_input != 'Y' and play_again_input != 'N':
                play_again_input = input("Please enter either Y or N.").upper()
            if play_again_input == 'Y':
                play_again = True
            else:
                play_again = False
    print("Thanks for playing Hangman!")

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
    play()

# call the main function
if __name__ == "__main__":
    main()
