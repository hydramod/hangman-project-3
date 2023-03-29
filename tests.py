import unittest
import io
import nltk
from nltk.corpus import wordnet
from unittest.mock import patch, call
from io import StringIO
from run import get_word, display_hangman, play, main, load_scores, save_scores, add_score, view_leaderboard, delete_score


class TestGetWordReturnsValidEnglishWordInUppercase(unittest.TestCase):

   def setUp(self):
      # Download the wordnet corpus before running tests
      nltk.download('wordnet')
      # Create a set of English words from the wordnet corpus
      self.english_words = set(wordnet.words())

   # Test that get_word() returns a valid English word in uppercase letters
   def test_get_word_returns_valid_word_in_uppercase(self):
      # get a 5-letter word
      word = get_word(5)
      # check that word is a string
      self.assertIsInstance(word, str)
      # check that word is in uppercase letters
      self.assertTrue(word.isupper())
      # check that lowercase version of word is a valid English word
      self.assertIn(word.lower(), self.english_words)

   def tearDown(self):
      # Download the wordnet corpus quietly after running tests
      nltk.download('wordnet', quiet=True)

class TestDisplayHangman(unittest.TestCase):

   # Test that display_hangman() returns the expected ASCII art for each try
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
      # Loop through each expected ASCII art and test that display_hangman() returns the correct output
      for tries in range(len(expected)):
         assert display_hangman(tries) == expected[tries]

class TestPlay(unittest.TestCase):

   @patch('builtins.input', side_effect=['1'])
   def test_play(self, mock_input):
      # Test that play() prompts the user to play the game and calls the function to start the game
      with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
         play()
         # get the value of stdout
         output = mock_stdout.getvalue()
         # check that prompt to play game is printed to stdout
         self.assertIn("Let's play Hangman!", output)

class TestMain(unittest.TestCase):

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

class TestLoadScores(unittest.TestCase):
    
   @patch('run.LEADERBOARD.get_all_records')
   def test_load_scores_returns_records(self, mock_get_all_records):
      # Set up mock return value
      mock_records = [{'Name': 'John', 'Score': 100}, {'Name': 'Jane', 'Score': 90}]
      mock_get_all_records.return_value = mock_records
      
      # Call the function and check the return value
      result = load_scores()
      self.assertEqual(result, mock_records)

class TestSaveScores(unittest.TestCase):
    
   @patch('run.LEADERBOARD.clear')
   @patch('run.LEADERBOARD.insert_row')
   def test_save_scores_clears_and_inserts_rows(self, mock_insert_row, mock_clear):
      # Set up mock input
      mock_scores = [{'Name': 'John', 'Score': 100}, {'Name': 'Jane', 'Score': 90}]
      
      # Call the function
      save_scores(mock_scores)
      
      # Check that clear() and insert_row() have been called with the correct arguments
      mock_clear.assert_called_once()
      mock_insert_row.assert_has_calls([call(['Rank', 'Name', 'Score'], 1),
                                       call([1, 'John', 100], 2),
                                       call([2, 'Jane', 90], 3)])
                                          
class TestAddScore(unittest.TestCase):
    
   @patch('run.input')
   @patch('run.load_scores')
   @patch('run.save_scores')
   def test_add_score_new_player(self, mock_save_scores, mock_load_scores, mock_input):
      # Set up mock inputs
      mock_input.side_effect = ['John', 'testword']
      mock_load_scores.return_value = []
      
      # Call the function
      add_score('testword')
      
      # Check that the new score was saved
      mock_save_scores.assert_called_once_with([{'Name': 'John', 'Score': 8}])
      
   @patch('run.input')
   @patch('run.load_scores')
   @patch('run.save_scores')
   def test_add_score_existing_player(self, mock_save_scores, mock_load_scores, mock_input):
      # Set up mock inputs
      mock_input.side_effect = ['John', 'testword']
      mock_load_scores.return_value = [{'Name': 'John', 'Score': 100}]
      
      # Call the function
      add_score('testword')
      
      # Check that the existing score was updated
      mock_save_scores.assert_called_once_with([{'Name': 'John', 'Score': 108}])
        
class TestViewLeaderboard(unittest.TestCase):
    
   @patch('run.load_scores')
   def test_view_leaderboard_no_scores(self, mock_load_scores):
      # Set up mock input
      mock_load_scores.return_value = []
      
      # Call the function
      with patch('builtins.print') as mock_print:
         view_leaderboard()
      
      # Check that the expected message was printed
      mock_print.assert_called_once_with('No scores found.')
      
   @patch('run.load_scores')
   def test_view_leaderboard_with_scores(self, mock_load_scores):
      # Set up mock input
      mock_scores = [{'Name': 'John', 'Score': 100}, {'Name': 'Jane', 'Score': 90}]
      mock_load_scores.return_value = mock_scores

class TestDeleteScore(unittest.TestCase):

   @patch('sys.stdout', new_callable=io.StringIO)
   @patch('builtins.input', return_value='John')
   def test_delete_score_deletes_player(self, mock_input, mock_stdout):
      # Set up test data
      player = [{'Name': 'John', 'Score': 100}]
      save_scores(player)

      # Call the function with test data
      with patch('run.load_scores', return_value=player), \
           patch('run.save_scores') as mock_save_scores:
         delete_score()

      # Check that the player was deleted
      updated_player = load_scores()
      self.assertNotIn({'Name': 'John', 'Score': 100}, updated_player)

      # Check that the user was informed that the player was deleted
      expected_output = "Deleted player: John\n"
      self.assertEqual(mock_stdout.getvalue(), expected_output)

   @patch('sys.stdout', new_callable=io.StringIO)
   @patch('builtins.input', return_value='Jane')
   def test_delete_score_player_not_found(self, mock_input, mock_stdout):
      # Set up test data
      player = [{'Name': 'John', 'Score': 100}]
      save_scores(player)

      # Call the function with test data
      with patch('run.load_scores', return_value=player), \
            patch('run.save_scores') as mock_save_scores:
         delete_score()

      # Check that the user was informed that the player was not found
      expected_output = "No player with name 'Jane' found.\n"
      self.assertEqual(mock_stdout.getvalue(), expected_output)