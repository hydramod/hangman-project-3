import unittest
import nltk
from nltk.corpus import words
from run import get_word, display_hangman

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