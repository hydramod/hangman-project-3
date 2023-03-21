## Hangman Game

This is a console-based Hangman game written in Python. The game randomly selects a word from the English dictionary and the player has to guess the word by suggesting letters or the complete word. The player has six tries to guess the word. For each incorrect guess, a part of the hangman figure is drawn. If the player is unable to guess the word within six tries, the game ends and the word is revealed.

## Requirements

The following modules are required to run this code:

- random
- nltk
- nltk.corpus
- The words corpus from the nltk library also needs to be downloaded before running the code.

## How to run the game

Clone the repository to your local machine.
Open a terminal window and navigate to the project directory.
Run the following command to start the game:
Copy code
python hangman.py

## How to play

The game will select a random word.
The player must guess the word by suggesting letters or the complete word.
If the suggestion is a single letter, the game will check if the letter is present in the word.
If the suggestion is the complete word, the game will check if the word is correct.
For each incorrect guess, a part of the hangman figure will be drawn.
The player has six tries to guess the word.
If the player guesses the word correctly, they win the game.
If the player is unable to guess the word within six tries, they lose the game and the word is revealed.
The player can choose to play again or exit the game.

## Function details

- get_word()
This function selects a random word from the English dictionary and returns it in uppercase.

- display_hangman(tries)
This function takes the number of tries as input and returns the ASCII art for the corresponding state of the hangman.

- play()
This is the main function that runs the game. It initializes the game by selecting a random word, setting the word completion status to underscores, and initializing the number of tries to six. It then prompts the player to guess a letter or word and continues until the player guesses the word correctly or runs out of tries.

- main()
This function calls the play() function to start the game.