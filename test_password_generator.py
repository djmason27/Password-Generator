"""Unit tests for the password generator."""

import re
import tempfile
import unittest
from pathlib import Path

from password_generator import DEFAULT_WORD_LIST, PasswordGenerator


class PasswordGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.output_path = Path(self.temporary_directory.name)
        self.generator = PasswordGenerator(self.output_path)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_memorable_password_format_and_log(self) -> None:
        password = self.generator.memorable_password(4, "lower", DEFAULT_WORD_LIST)
        self.assertEqual(len(password.split("-")), 4)
        self.assertTrue(all(re.fullmatch(r"[a-z]+\d", part) for part in password.split("-")))
        log = self.output_path / "Memorable" / "Generated_Passwords.txt"
        self.assertTrue(log.exists())
        self.assertIn(password, log.read_text(encoding="utf-8"))

    def test_random_password_options_and_log(self) -> None:
        password = self.generator.random_password(40, False, "aA0")
        self.assertEqual(len(password), 40)
        self.assertFalse(any(char in password for char in "aA0"))
        self.assertTrue(all(char.isalnum() for char in password))
        log = self.output_path / "Random" / "Generated_Passwords.txt"
        self.assertTrue(log.exists())

    def test_invalid_arguments(self) -> None:
        with self.assertRaises(ValueError):
            self.generator.memorable_password(0, "lower", DEFAULT_WORD_LIST)
        with self.assertRaises(ValueError):
            self.generator.memorable_password(2, "sideways", DEFAULT_WORD_LIST)
        with self.assertRaises(ValueError):
            self.generator.random_password(0)


if __name__ == "__main__":
    unittest.main()
