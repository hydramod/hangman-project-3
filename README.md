# Hangman Game

```python

888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"  

```

This is a console-based Hangman game written in Python. The game randomly selects a word from the English dictionary and the player has to guess the word by suggesting letters or the complete word. The player has six tries to guess the word. For each incorrect guess, a part of the hangman figure is drawn. If the player is unable to guess the word within six tries, the game ends and the word is revealed.

## Requirements

The following modules are required to run this code:

- random
- gspread
- nltk
- nltk.corpus
- The words corpus from the nltk library also needs to be downloaded before running the code.

Run the following command to install requirements:
```
pip install -r requirements.txt
```

## How to run the game

1. Clone the repository to your local machine.
2. Go to the Google Cloud Console: https://console.cloud.google.com/
3. If you do not already have a Google Cloud Platform account, you will need to create one. If you do have an account, log in to the console.
4. Once you are logged in, click on the project dropdown menu at the top of the screen and select "New Project".
5. In the "New Project" dialog box, enter a name for your project and click "Create".
6. Once your project has been created, you will be taken to the project dashboard. Click on the "APIs & Services" menu in the left sidebar and select "Dashboard".
7. Click on the "+ ENABLE APIS AND SERVICES" button at the top of the page.
8. Search for "Google Sheets API" and "Google Drive API" in the search bar and select them.
9. Click the "Enable" button to enable both APIs for your project.
10. Next, you will need to create credentials for your project. Click on "Create Credentials" and select "Service Account Key".
11. Fill in the required fields for the service account, such as the service account name and role. Choose "JSON" as the key type and click "Create".
12. Save the generated JSON file to your local computer and rename it as "creds.json". This file contains the private key for your service account.
13. Finally, you can use the credentials and APIs to access your Google Sheets and Google Drive data through your project.
14. Go to the Google Sheets page: https://docs.google.com/spreadsheets.
15. Click the "Blank" button in the upper left corner under "Start a new spreadsheet".
16. Rename the spreadsheet to "Hangman" by doub-clicking on the title in the upper left corner.
17. Rename the default sheet to "Leaderboard" by double-clicking on the tab at the bottom and typing in the new name.
18. Populate the first row with the necessary headers for your Leaderboard. (Rank, Name, Score)
19. Click the "Share" button in the upper right corner of the page.
20. In the "Share with people and groups" section, enter the email address of the google service account email from your credentials JSON you have downloaded to share the document with.
21. Choose the level of access you want to grant "Can Edit".
22. Click the "Send" button to share the document.
23. Move the creds.json file into the root directory of the hangman game.
24. Open a terminal window and navigate to the project directory.

Run the following command to start the game:
```
python run.py
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

- nltk.download('wordnet'):
Downloads the words corpus from the Natural Language Toolkit (nltk) library.

- title():
This function is a simple helper function that prints the title of the game

- select_difficulty_level():
Function prompts the user to select a difficulty level and returns the maximum number of characters and hints allowed for the word, based on the user's input.

- get_word(max_length):
This function selects a random word depending on the max length set by the difficulty level from the English dictionary and returns it in uppercase.

- display_hangman(tries):
This function takes the number of tries as input and returns the ASCII art for the corresponding state of the hangman.

- load_scores():
This function retrieves all records from Google Sheets and returns them as a list of dictionaries.

- save_scores(scores):
This function clears all existing records in the Google Sheets, inserts a header row at the top of the sheet, and loops through each score to insert it as a new row in the Google Sheets.

- add_score(word):
This function prompts the user to enter their name, calculates their score based on the length of the input word, loads the leaderboard scores, checks if the player already exists, and either adds points to their existing score or adds a new score to the leaderboard.

- view_leaderboard():
This function loads the scores from the file, checks if there are any scores, and if there are, prints the leaderboard header and loops through the scores to print each one.

- delete_score():
This function prompts the user to enter the name of the player to delete, loads the scores from the file, creates a new list of scores without the specified player, saves the updated scores to the file, and informs the user that the player was deleted.

- leaderboard_menu():
This function displays a menu of options for the user to choose from (view leaderboard, delete score, or return to the main menu) and processes the user's choice by calling the corresponding function.

- play():
This is the main function that runs the game. It initializes the game by selecting a random word depending on the difficulty selected by the user, setting the word completion status to underscores, and initializing the number of tries to six. It then prompts the player to guess a letter or word and continues until the player guesses the word correctly or runs out of tries.

- hint(word):
Function to provide a hint for the hangman game. It reveals a random letter from the word that hasn't been guessed yet along with the word definition.

- play_again_input():
Function prompts the user to play again and returns True if the user enters 'Y' or False if the user enters 'N'.

- main():
This function calls the play() function to start the game.

## Game Testing

### Automated Testing

Test requirements
The following modules are required to run the test code:

- unittest
- io
- nltk
- nltk.corpus
- unittest.mock
- The words corpus from the nltk library also needs to be downloaded before running the code.

Run the following command to start the tests:
```
python -m unittest tests.py
```

Initiatiing the Test class to run the following test cases

```python
class Test(unittest.TestCase):
```

1. Unit test the "get_word" function to ensure it returns a valid word in uppercase letters from the nltk corpus.

- This test can be passed by verifying that the output of the "get_word" function is a string of uppercase letters that is a valid English word in the nltk corpus. We can use the following code to perform this test:

```python
    def setUp(self):
        nltk.download('wordnet')
        self.english_words = set(wordnet.words())

    def test_get_word_returns_valid_word_in_uppercase(self):
        word = get_word()
        self.assertIsInstance(word, str)
        self.assertTrue(word.isupper())
        self.assertIn(word.lower(), self.english_words)

    def tearDown(self):
        nltk.download('wordnet', quiet=True)
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

3. Test the "main" function to ensure it correctly calls the "play" function when executed.

- To test the "main" function, we can use the unittest framework to mock the "play" function and then verify that the "play" function is called when the "main" function is executed. We can use the following code to perform this test:

```python
@patch('builtins.input', side_effect=['1'])
   def test_play(self, mock_input):
      # Test that play() prompts the user to play the game and calls the function to start the game
      with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
         play()
         # get the value of stdout
         output = mock_stdout.getvalue()
         # check that prompt to play game is printed to stdout
         self.assertIn("Let's play Hangman!", output)

@patch('builtins.input', side_effect=['3']) # changed the value to '3'
def test_main(self, mock_input):
   # Test that main() prompts the user to play the game and calls the function to start the game
   with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      # patch the main() function so that it does not execute during testing
      main()
      # get the value of stdout
      output = mock_stdout.getvalue()
      # Assert that the main() function has been called
      self.assertIn("1. Start a new game", output)
```

The StopIteration error which occurs when there are no more items left to iterate over. This error is caused by the mock_input object running out of values to return when input is called in the main function. To prevent this a try except was added to run.py

```python
try:
   guess = input("Please guess a letter or word: ").upper()
      except StopIteration:
   return
```

4. Test the entire code by running it and playing the game to ensure it functions correctly and the game is enjoyable.

- To test the entire code by running it and playing the game, we can manually play the game and verify that it functions correctly and is enjoyable.

Results for the automated and manual test have passed as expected, however on initial start of the unittest, the first run fails, this is due to nltk test first downloading the dictionary. Upon the second run All automated test pass with no issue. The game functions and plays as expected.

![Hangman test](/docs/images/tests.png)

### Manual Testing

1. Test the "select_difficulty_level" function with valid inputs to ensure it correctly initializes the game according to selected difficulty.

![Hangman select difficulty](/docs/images/difficulty.png)

- This test can be passed by manually playing the game and verifying that it, accepts valid numeric inputs, and correctly initializes the game according to the difficulty selected.

2. Test the "play" function with valid inputs to ensure it correctly initializes the game and allows the user to input valid guesses for both letters and words until they either win or lose.

![Hangman start](/docs/images/start.png)

- This test can be passed by manually playing the game and verifying that it initializes correctly, accepts valid guesses for both letters and words, and correctly determines whether the user has won or lost the game. This test cannot be fully automated as it requires user input.

3. Test the "play" function with invalid inputs to ensure it correctly handles and displays error messages for invalid guesses.

![Hangman input not valid](/docs/images/not%20valid.png)

- The "play" function was tested by inputting invalid characters (such as numbers, symbols, or non-English letters) as guesses for both letters and words. The function handled the input errors correctly by displaying a message informing the user of the invalid input and prompting them to try again with a valid guess.

4. Test the "play" function by intentionally losing the game to ensure it correctly displays the word and prompts the user to play again.

![Hangman lose](/docs/images/lose.png)

- To test the "play" function by intentionally losing the game, we can set the number of maximum incorrect guesses to 1 and then guess an incorrect letter to trigger the game over condition. We can then verify that the function correctly displays the word and prompts the user to play again.

5. Test the "play" function by intentionally winning the game to ensure it correctly prompts the user to play again.

![Hangman win](/docs/images/win.png)

- To test the "play" function by intentionally winning the game, we can set the maximum number of incorrect guesses to a large number (e.g., 10) and then guess all the correct letters in the word to trigger the win condition. We can then verify that the function correctly prompts the user to play again. 

## Technologies

- Python for functionality and game logic
- Developed using Visual Studio Code IDE
- Source code hosted on GitHub, deployed with Heroku
- Git used for code management

## Deployment

The game was uploaded to a cloud platform called Heroku. To do this, a new application was created and named in the settings tab.

Additionally, buildpacks for both Python and Node.js were added in that order by selecting "Add buildpack". This ensures that the necessary dependencies are installed and configured correctly on Heroku.

To deploy the app, the "Deployment Method" was selected under the Deploy tab, and then "GitHub" was clicked to connect to the relevant repository. "Enable Automatic Deploys" was also selected so that the app could be rebuilt automatically every time changes were pushed to GitHub.

Here is the link to the app where it is currently deployed: https://hangman-ci-project-3.herokuapp.com

## Credits

- Documentaion on the [unittest framework](https://docs.python.org/3/library/unittest.html)
- Documentation on the [Natural Languange Tool Kit](https://www.nltk.org/index.html#)
- Repurposed my [moviedb project](https://github.com/hydramod/moviedb-project-3) to handle the leaderboard system 
- Information for [ansi escape code colors](https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803)
- Inspiration for [ASCII art](https://codegolf.stackexchange.com/questions/135936/ascii-hangman-in-progress)
- Inspiration for [ASCII art](https://ascii.co.uk/art/hangman)
- Inspration for this project from [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8)
- Thank you google for everything else.
