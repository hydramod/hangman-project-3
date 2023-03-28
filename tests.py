import unittest
import io
import nltk
from nltk.corpus import wordnet
from unittest.mock import patch
from io import StringIO
from run import get_word, display_hangman, play, main


class Test(unittest.TestCase):

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