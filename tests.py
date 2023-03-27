import unittest
import io
import nltk
from nltk.corpus import wordnet
from unittest.mock import patch
from io import StringIO
from run import get_word, display_hangman, play, main


class Test(unittest.TestCase):

   def setUp(self):
      nltk.download('wordnet')
      self.english_words = set(wordnet.words())

   def test_get_word_returns_valid_word_in_uppercase(self):
      word = get_word(5)
      self.assertIsInstance(word, str)
      self.assertTrue(word.isupper())
      self.assertIn(word.lower(), self.english_words)

   def tearDown(self):
      nltk.download('wordnet', quiet=True)

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

   @patch('builtins.input', side_effect=['1', '2', '3', '4'])
   def test_play(self, mock_input):
      with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
         play()
         output = mock_stdout.getvalue()
         self.assertIn("Let's play Hangman!", output)

   @patch('builtins.input', side_effect=['y', 'n'])
   def test_main(self, mock_input):
      with patch('run.play') as mock_play:
         main()
         mock_play.assert_called()
   

