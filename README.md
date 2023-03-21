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
```
python hangman.py
```
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
class TestGetWord(unittest.TestCase):

    def setUp(self):
        nltk.download('words')
        self.english_words = set(words.words())

    def test_get_word_returns_valid_word_in_uppercase(self):
        word = get_word()
        self.assertIsInstance(word, str)
        self.assertTrue(word.isupper())
        self.assertIn(word.lower(), self.english_words)

    def tearDown(self):
        nltk.download('words', quiet=True)
```
In this test, we first download the English words from the nltk corpus in the setUp method. We then define the test_get_word_returns_valid_word_in_uppercase method, which calls the get_word function and verifies that the returned word is a string of uppercase letters that is a valid English word in the nltk corpus. We use the isinstance function to verify that the returned word is a string, the isupper method to verify that it is in uppercase letters, and the assertIn method to verify that the lowercase version of the word is in the set of English words. We also use the tearDown method to clean up after the test, by downloading the nltk corpus again with the quiet argument set to True to suppress any output.

2. Unit test the "display_hangman" function to ensure it returns the correct ASCII art representation of the hangman at each stage.

- This test can be passed by manually comparing the output of the "display_hangman" function at each stage to the expected ASCII art representation of the hangman. Alternatively we can use the following code to perform this test:

```python
def test_display_hangman(self):
        expected = [  # final state: head, torso, both arms, and both legs
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
        for tries in range(len(expected)):
            assert display_hangman(tries) == expected[tries]
```
This test compares the output of the "display_hangman" function at each stage to the expected ASCII art representation of the hangman.

3. Test the "play" function with valid inputs to ensure it correctly initializes the game and allows the user to input valid guesses for both letters and words until they either win or lose.

- This test can be passed by manually playing the game and verifying that it initializes correctly, accepts valid guesses for both letters and words, and correctly determines whether the user has won or lost the game. This test cannot be fully automated as it requires user input. We can manually play the game and verify that it initializes correctly, accepts valid guesses for both letters and words, and correctly determines whether the user has won or lost the game.

4. Test the "play" function with invalid inputs to ensure it correctly handles and displays error messages for invalid guesses.

- The "play" function was tested by inputting invalid characters (such as numbers, symbols, or non-English letters) as guesses for both letters and words. The function handled the input errors correctly by displaying a message informing the user of the invalid input and prompting them to try again with a valid guess.

5. Test the "play" function by intentionally losing the game to ensure it correctly displays the word and prompts the user to play again.

- To test the "play" function by intentionally losing the game, we can set the number of maximum incorrect guesses to 1 and then guess an incorrect letter to trigger the game over condition. We can then verify that the function correctly displays the word and prompts the user to play again. We can use the following code to perform this test:

```python
def test_play_lose():
    word = get_word()
    max_incorrect_guesses = 1
    incorrect_guesses = 0
    guessed_letters = set()
    guessed_words = set()
    while incorrect_guesses < max_incorrect_guesses:
        guess = "x"  # guess an incorrect letter
        if guess not in guessed_letters:
            guessed_letters.add(guess)
            if guess in word:
                print("Correct!")
            else:
                print("Incorrect!")
                incorrect_guesses += 1
        else:
            print("You already guessed that letter!")
    print(f"The word was {word}.")
    assert play(max_incorrect_guesses) == False
```

6. Test the "play" function by intentionally winning the game to ensure it correctly prompts the user to play again.

- To test the "play" function by intentionally winning the game, we can set the maximum number of incorrect guesses to a large number (e.g., 10) and then guess all the correct letters in the word to trigger the win condition. We can then verify that the function correctly prompts the user to play again. We can use the following code to perform this test:

```python
def test_play_win():
    word = get_word()
    max_incorrect_guesses = 10
    incorrect_guesses = 0
    guessed_letters = set()
    guessed_words = set()
    while incorrect_guesses < max_incorrect_guesses and set(word) != guessed_letters:
        guess = word[0]  # guess a correct letter
        if guess not in guessed_letters:
            guessed_letters.add(guess)
            if guess in word:
                print("Correct!")
            else:
                print("Incorrect!")
                incorrect_guesses += 1
        else:
            print("You already guessed that letter!")
    assert play(max_incorrect_guesses) == True
```

7. Test the "main" function to ensure it correctly calls the "play" function when executed.

- To test the "main" function, we can use the unittest framework to mock the "play" function and then verify that the "play" function is called when the "main" function is executed. We can use the following code to perform this test:

```python
import unittest
from unittest.mock import patch

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_main(self, mock_input):
        with patch('game.play') as mock_play:
            main()
            mock_play.assert_called()
```

8. Test the entire code by running it and playing the game to ensure it functions correctly and the game is enjoyable.

- To test the entire code by running it and playing the game, we can manually play the game and verify that it functions correctly and is enjoyable. We can use the following code to run the game:

```python
if __name__ == '__main__':
    main()
```
