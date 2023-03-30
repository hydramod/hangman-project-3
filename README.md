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

The following modules are required to run the test code:

- unittest
- io
- nltk
- nltk.corpus
- unittest.mock
- The words corpus from the nltk library also needs to be downloaded before running the code.

Run the following command to start the tests:
```
python -m unittest -vv tests.py
```

#### 1. TestGetWordReturnsValidEnglishWordInUppercase
Tests the get_word() function to ensure that it returns a valid English word in uppercase letters.

test_get_word_returns_valid_word_in_uppercase
- Downloads the wordnet corpus and creates a set of English words from the wordnet corpus.
- Calls get_word() function to get a 5-letter word.
- Asserts that the returned value is of type string.
- Asserts that the returned string is in uppercase letters.
- Asserts that the lowercase version of the returned word is a valid English word.

#### 2. TestDisplayHangman
Tests the display_hangman() function to ensure that it returns the expected ASCII art for each try.

test_display_hangman
- Defines a list of expected output strings, one for each possible state of the hangman.
- Loops through each expected output string and tests that display_hangman() returns the correct output string.

#### 3. TestPlay
Tests the play() function to ensure that it prompts the user to play the game and calls the function to start the game.

test_play
- Uses the @patch decorator to patch the built-in input() function so that it returns the value 1 (which corresponds to "Yes" when asked to play the game).
- Uses the with statement to capture the output of play() function when called.
- Asserts that the prompt to play the game is printed to the captured output.

The StopIteration error which occurs when there are no more items left to iterate over. This error is caused by the mock_input object running out of values to return when input is called in the main function. To prevent this a try except was added to run.py

```python
try:
   guess = input("Please guess a letter or word: ").upper()
      except StopIteration:
   return
```

#### 4. TestMain
Tests the main() function to ensure that it prompts the user to play the game and calls the function to start the game.

test_main
- Uses the @patch decorator to patch the built-in input() function so that it returns the value 3 (which corresponds to "Quit" when asked to play the game).
- Uses the with statement to capture the output of main() function when called.
- Asserts that the prompt to start a new game is printed to the captured output.

#### 5. TestLoadScores
Tests the load_scores() function to ensure that it returns the correct list of scores.

test_load_scores_returns_records
- Uses the @patch decorator to patch the get_all_records() method of the LEADERBOARD object so that it returns a mock list of records.
- Calls the load_scores() function.
- Asserts that the returned value is equal to the mock list of records.

#### 6. TestSaveScores
Tests the save_scores() function to ensure that it clears the leaderboard and inserts the correct rows.

test_save_scores_clears_and_inserts_rows
- Defines a mock list of scores.
- Calls the save_scores() function with the mock list of scores.
- Uses the assert_called_once() method to assert that the clear() method of the LEADERBOARD object has been called once.
- Uses the assert_has_calls() method to assert that the insert_row() method of the LEADERBOARD object has been called with the correct arguments.

#### 7. TestAddScore
test_add_score_new_player
- Tests that add_score correctly saves a new player's score when given a new player name and a new score.
- mock_input.side_effect = ['John', 'testword']: Sets up mock user input to simulate the user entering "John" as the player name and "testword" as the word to be scored.
- mock_load_scores.return_value = []: Sets up a mock return value for load_scores to simulate an empty list of scores.
- add_score('testword'): Calls add_score with the mock input and mock return values.
- mock_save_scores.assert_called_once_with([{'Name': 'John', 'Score': 8}]): Checks that save_scores was called with a list containing a dictionary representing the new player and their score.

test_add_score_existing_player
- Tests that add_score correctly updates an existing player's score when given an existing player name and a new score.
- mock_input.side_effect = ['John', 'testword']: Sets up mock user input to simulate the user entering "John" as the player name and "testword" as the word to be scored.
- mock_load_scores.return_value = [{'Name': 'John', 'Score': 100}]: Sets up a mock return value for load_scores to simulate a list containing one dictionary representing an existing player with a score of 100.
- add_score('testword'): Calls add_score with the mock input and mock return values.
- mock_save_scores.assert_called_once_with([{'Name': 'John', 'Score': 108}]): Checks that save_scores was called with a list containing a dictionary representing the existing player with their score updated to 108.

#### 8. TestViewLeaderboard
test_view_leaderboard_no_scores
Tests that view_leaderboard correctly prints a message when there are no scores to display.
- mock_load_scores.return_value = []: Sets up a mock return value for load_scores to simulate an empty list of scores.
- with patch('builtins.print') as mock_print: view_leaderboard(): Calls view_leaderboard and captures the printed output in a mock print statement.
- mock_print.assert_called_once_with('No scores found.'): Checks that the mock print statement was called with the expected message.

test_view_leaderboard_with_scores
- Tests that view_leaderboard correctly prints the leaderboard when there are scores to display.
- mock_scores = [{'Name': 'John', 'Score': 100}, {'Name': 'Jane', 'Score': 90}]: Sets up a mock list of scores containing two dictionaries representing players and their scores.
- mock_load_scores.return_value = mock_scores: Sets up a mock return value for load_scores to simulate the list of scores.
- view_leaderboard(): Calls view_leaderboard.
- The test case does not include an explicit check on the printed output, but the function's correct execution is implied by the lack of assertion errors.

#### 9. TestDeleteScore
test_delete_score_deletes_player:
- Tests that delete_score correctly deletes a player from the list of scores when given the name of an existing player.
- Sets up a mock list of scores containing one dictionary representing an existing player with a score of 100.
- Calls delete_score with the mock list of scores and the name of the player to be deleted.
- Checks that the player was deleted from the list of scores.
- Checks that the user was informed that the player was deleted.

test_delete_score_player_not_found:
- Tests that delete_score correctly handles the case when a non-existent player name is provided.
- Sets up a mock list of scores containing one dictionary representing an existing player with a score of 100.
- Calls delete_score with the mock list of scores and the name of a non-existent player.
- Checks that the user was informed that no player with the given name was found.

- Both test cases use the @patch decorator to mock the input and output streams of the delete_score function, and the load_scores and save_scores functions that it calls internally. This allows the test cases to provide controlled inputs and observe the outputs and side effects of the function under test.

#### Results
Overall the automated tests have passed and are summarized in this test log
```
- [nltk_data] Downloading package wordnet to /home/gitpod/nltk_data...
- [nltk_data]   Package wordnet is already up-to-date!
- test_add_score_existing_player (tests.TestAddScore) ... Added 8 points to John. New score: 108
ok
- test_add_score_new_player (tests.TestAddScore) ... Added score: John - 8
ok
- test_delete_score_deletes_player (tests.TestDeleteScore) ... ok
- test_delete_score_player_not_found (tests.TestDeleteScore) ... ok
- test_display_hangman (tests.TestDisplayHangman) ... ok
- test_get_word_returns_valid_word_in_uppercase (tests.TestGetWordReturnsValidEnglishWordInUppercase) ... [nltk_data] Downloading package wordnet to /home/gitpod/nltk_data...
- [nltk_data]   Package wordnet is already up-to-date!
ok
- test_load_scores_returns_records (tests.TestLoadScores) ... ok
- test_main (tests.TestMain) ... ok
- test_play (tests.TestPlay) ... ok
- test_save_scores_clears_and_inserts_rows (tests.TestSaveScores) ... ok
- test_view_leaderboard_no_scores (tests.TestViewLeaderboard) ... ok
- test_view_leaderboard_with_scores (tests.TestViewLeaderboard) ... ok

----------------------------------------------------------------------
- Ran 12 tests in 5.780s

- OK
```

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

### Code Validator Test

Two validators were used for this [pep8ci]([pep8ci](https://pep8ci.herokuapp.com/)) and pycodestyle, pycodestyle is meant to be the replacement for pep8 which is why i have used it here.

To run the validator the pycodestyle module is required

```
pip install pycodestyle
```

Once installed run the following commands:
```
pycodestyle run.py
```

```
pycodestyle tests.py
```

The pycodestyle validator will output nothing if the code passes with no errors. 
You can run the following commands to see the full output of the pycodestyle validator if you wish:
```
pycodestyle -vv run.py
```

```
pycodestyle -vv tests.py
```

Both run.py and tests.py pass the pycodestyle and the pep8 validator. with no errors

- run.py
```
All clear, no errors found
```

tests.py
```
All clear, no errors found
```

## Flowcharts

Two different tools were used to generate flowcharts - Lucidchart and PyCharm's diagram tool. The main game flow was created using Lucidchart as it was visually appealing and presented the information in a clear and easy-to-understand manner. On the other hand, PyCharm's diagram tool was utilized to represent the test flow as it provided the most detailed and comprehensive information about the tests conducted. In summary, each tool was chosen based on its strengths and suitability for the specific task at hand.

### Hangman game flowchart

![Hangman Flowchart](/docs/images/Flowchart%20Hangman.png)

### Automated tests flowchart

![Hangman Tests Flowchart](/docs/images/tests%20flow.png)

## Technologies

- Python for functionality and game logic
- Developed using Visual Studio Code IDE
- Source code hosted on GitHub, deployed with Heroku
- Git used for code management
- Lucidchart and pycharm for generation of flowcharts

A brief description of the purpose of each module used in this code:

The main game modules:
- random: This module provides functions for generating random numbers, which is used in the Hangman game to select a random word from a list of possible words.
- os: This module provides a way to interact with the operating system, and is used in the Hangman game to clear the console screen after each guess.
- nltk: The Natural Language Toolkit (NLTK) is a platform for building Python programs to work with human language data. It is used in the Hangman game to check if the guessed letter is a valid English alphabet or not.
- nltk.corpus: This sub-module of NLTK provides access to a variety of linguistic data, such as word lists and corpora. In the Hangman game, it is used to access the wordnet corpus, which is a lexical database of English words.
- gspread: This module allows programmatic access to Google Sheets, and is used in the Hangman game to write the game's statistics to a Google Sheet.
- google.oauth2.service_account: This module provides a way to authenticate using a service account to access Google APIs, and is used in the Hangman game to authenticate the program to write to a Google Sheet.

The test modules are as follows:
- unittest: a built-in Python module that provides a framework for writing and running unit tests. It includes various assertion methods and test runners for automated testing of Python code.
- io: a built-in Python module that provides a set of functions for working with streams of data.
- wordnet: a sub-module of the NLTK library that provides access to the WordNet lexical database, which includes English words grouped into synonym sets (synsets) and organized by semantic relationships such as hypernymy (i.e., "is a" relationships).
- unittest.mock: a built-in Python module that provides tools for mocking and patching objects and functions in unit tests.
- patch: a decorator in the unittest.mock module that can be used to temporarily replace an object or function with a mock object or function during a test.
- call: a class in the unittest.mock module that represents a call to a mock object or function, including its arguments and return value.
- StringIO: a class in the io module that provides a way to create a stream of text data in memory that can be read from or written to like a file. This is useful for capturing output from functions or for testing functions that expect a file-like object as input.
- run: a custom Python module that contains the functions to be tested. The module includes functions for loading and saving high scores, playing the hangman game, and displaying the leaderboard.

## Deployment

The game was uploaded to a cloud platform called Heroku. To do this, a new application was created and named in the settings tab.

Configuration variables that include the required Google API credentials were set under the config vars key.

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
- Thank you to Gareth McGirr for the great feedback and support.
- Thank you google for everything else.
