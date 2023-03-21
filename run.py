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
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
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

# function to display the hangman
def display_hangman(tries):
    print("PLACEHOLDER FOR HANGMAN")

# main function to start the game
def main():
    #word = get_word()
    play()
    #print(word)

# call the main function
if __name__ == "__main__":
    main()
