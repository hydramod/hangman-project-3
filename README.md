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

Both run.py and tests.py pass the pycodestyle validator, however with one annoyance, the validator flags my comments as being over 79 characters long, however this does not have any negative impact on code functionality. Keeping comments as is gives good insight on how the code functions and helps with future development if required.

- run.py
```
run.py:26:80: E501 line too long (84 > 79 characters)
run.py:30:80: E501 line too long (83 > 79 characters)
run.py:37:80: E501 line too long (82 > 79 characters)
run.py:50:80: E501 line too long (122 > 79 characters)
run.py:64:80: E501 line too long (105 > 79 characters)
run.py:87:80: E501 line too long (109 > 79 characters)
run.py:92:80: E501 line too long (96 > 79 characters)
run.py:96:80: E501 line too long (101 > 79 characters)
run.py:102:80: E501 line too long (98 > 79 characters)
run.py:116:80: E501 line too long (117 > 79 characters)
run.py:118:80: E501 line too long (115 > 79 characters)
run.py:128:80: E501 line too long (90 > 79 characters)
run.py:132:80: E501 line too long (135 > 79 characters)
run.py:138:80: E501 line too long (109 > 79 characters)
run.py:148:80: E501 line too long (118 > 79 characters)
run.py:153:80: E501 line too long (88 > 79 characters)
run.py:158:80: E501 line too long (95 > 79 characters)
run.py:164:80: E501 line too long (85 > 79 characters)
run.py:178:80: E501 line too long (81 > 79 characters)
run.py:183:80: E501 line too long (89 > 79 characters)
```

tests.py
```
tests.py:7:80: E501 line too long (122 > 79 characters)
tests.py:12:80: E501 line too long (99 > 79 characters)
tests.py:114:80: E501 line too long (105 > 79 characters)
tests.py:121:80: E501 line too long (95 > 79 characters)
tests.py:136:80: E501 line too long (95 > 79 characters)
tests.py:142:80: E501 line too long (82 > 79 characters)
tests.py:152:80: E501 line too long (92 > 79 characters)
tests.py:168:80: E501 line too long (108 > 79 characters)
tests.py:173:80: E501 line too long (84 > 79 characters)
tests.py:179:80: E501 line too long (89 > 79 characters)
tests.py:188:80: E501 line too long (118 > 79 characters)
tests.py:194:80: E501 line too long (88 > 79 characters)
tests.py:209:80: E501 line too long (93 > 79 characters)
```

## Technologies

- Python for functionality and game logic
- Developed using Visual Studio Code IDE
- Source code hosted on GitHub, deployed with Heroku
- Git used for code management

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
