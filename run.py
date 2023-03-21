import random
import nltk
from nltk.corpus import words

nltk.download('words')
english_words = words.words()

# function to choose a random word
def get_word():
    word = ""
    while not word.isalpha():
        word = random.choice(english_words)
    return word.upper()

# main function to start the game
def main():
    word = get_word()
    print(word)

# call the main function
if __name__ == "__main__":
    main()
