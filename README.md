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

## Game Testing

1. Unit test the "get_word" function to ensure it returns a valid word in uppercase letters from the nltk corpus.

- This test can be passed by verifying that the output of the "get_word" function is a string of uppercase letters that is a valid English word in the nltk corpus. We can use the following code to perform this test:

```python
def test_get_word():
    english_words = set(words.words())
    word = get_word()
    assert word.isalpha() and word.isupper() and word in english_words
```
This test downloads the English words from the nltk corpus, calls the "get_word" function to get a word, and then asserts that the word returned is a string of uppercase letters that is a valid English word in the nltk corpus.

2. Unit test the "display_hangman" function to ensure it returns the correct ASCII art representation of the hangman at each stage.

- This test can be passed by manually comparing the output of the "display_hangman" function at each stage to the expected ASCII art representation of the hangman. We can use the following code to perform this test:

```python
def test_display_hangman():
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
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
    for i in range(len(stages)):
        assert display_hangman(i) == stages[i]
```
This test compares the output of the "display_hangman" function at each stage to the expected ASCII art representation of the hangman.

3. Test the "play" function with valid inputs to ensure it correctly initializes the game and allows the user to input valid guesses for both letters and words until they either win or lose.

- This test can be passed by manually playing the game and verifying that it initializes correctly, accepts valid guesses for both letters and words, and correctly determines whether the user has won or lost the game. This test cannot be fully automated as it requires user input. We can manually play the game and verify that it initializes correctly, accepts valid guesses for both letters and words, and correctly determines whether the user has won or lost the game.

Test the "play" function with invalid inputs to ensure it correctly handles and displays error messages for invalid guesses.

Test the "play" function by intentionally losing the game to ensure it correctly displays the word and prompts the user to play again.

Test the "play" function by intentionally winning the game to ensure it correctly prompts the user to play again.

Test the "main" function to ensure it correctly calls the "play" function when executed.

Test the entire code by running it and playing the game to ensure it functions correctly and the game is enjoyable.