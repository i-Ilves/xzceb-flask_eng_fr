import unittest

from translator import english_to_french, french_to_english

class TestEnToFr(unittest.TestCase):
    """Class for testing function english_to_french"""
    def test1(self):
        """Test the function english_to_french"""
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestFrToEn(unittest.TestCase):
    """Class for testing function french_to_english"""
    def test1(self):
        """Test the function french_to_english"""
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

unittest.main()