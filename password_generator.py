"""Interactive and reusable memorable/random password generator."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import secrets
import string


BASE_DIRECTORY = Path(__file__).resolve().parent
DEFAULT_WORD_LIST = BASE_DIRECTORY / "sample_words.txt"


class PasswordGenerator:
    """Generate passwords and record each one with its creation time."""

    def __init__(self, output_directory: str | Path = BASE_DIRECTORY) -> None:
        self.output_directory = Path(output_directory)

    def _save_password(self, password: str, password_type: str) -> None:
        folder = self.output_directory / password_type
        folder.mkdir(parents=True, exist_ok=True)
        output_file = folder / "Generated_Passwords.txt"
        timestamp = datetime.now().strftime("%A, %B %d, %Y at %I:%M:%S %p")
        with output_file.open("a", encoding="utf-8") as file:
            file.write(f"{timestamp} | {password}\n")

    def memorable_password(
        self,
        number_of_words: int,
        available_cases: str = "mixed",
        word_list_path: str | Path = DEFAULT_WORD_LIST,
    ) -> str:
        """Generate words with one digit each, joined by hyphens.

        available_cases may be ``lower``, ``upper``, or ``mixed``. In mixed
        mode, every selected word is independently made lower- or uppercase.
        """
        if number_of_words < 1:
            raise ValueError("The number of words must be at least 1.")

        case_choice = available_cases.strip().lower()
        if case_choice not in {"lower", "upper", "mixed"}:
            raise ValueError("Available cases must be lower, upper, or mixed.")

        path = Path(word_list_path)
        if not path.exists():
            raise FileNotFoundError(f"Word-list file not found: {path}")

        with path.open("r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
        if not words:
            raise ValueError("The word-list file is empty.")

        pieces = []
        for _ in range(number_of_words):
            word = secrets.choice(words)
            if case_choice == "upper":
                word = word.upper()
            elif case_choice == "lower":
                word = word.lower()
            else:
                word = word.upper() if secrets.randbelow(2) else word.lower()
            pieces.append(f"{word}{secrets.choice(string.digits)}")

        password = "-".join(pieces)
        self._save_password(password, "Memorable")
        return password

    def random_password(
        self,
        length: int,
        include_punctuation: bool = True,
        disallowed_characters: str = "",
    ) -> str:
        """Generate a random password using the requested character options."""
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        characters = string.ascii_letters + string.digits
        if include_punctuation:
            characters += string.punctuation
        allowed = "".join(char for char in characters if char not in disallowed_characters)
        if not allowed:
            raise ValueError("The disallowed characters removed every available character.")

        password = "".join(secrets.choice(allowed) for _ in range(length))
        self._save_password(password, "Random")
        return password


def _ask_positive_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def _ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter yes or no.")


def main() -> None:
    """Run the interactive password generator."""
    generator = PasswordGenerator()
    while True:
        password_type = input("Choose password type (memorable/random): ").strip().lower()
        if password_type in {"memorable", "random"}:
            break
        print("Please enter memorable or random.")

    if password_type == "memorable":
        number_of_words = _ask_positive_integer("Number of words: ")
        while True:
            cases = input("Available cases (lower/upper/mixed): ").strip().lower()
            if cases in {"lower", "upper", "mixed"}:
                break
            print("Please enter lower, upper, or mixed.")
        custom_path = input(
            f"Word-list path (press Enter for {DEFAULT_WORD_LIST.name}): "
        ).strip()
        path = custom_path or DEFAULT_WORD_LIST
        password = generator.memorable_password(number_of_words, cases, path)
    else:
        length = _ask_positive_integer("Password length: ")
        punctuation = _ask_yes_no("Include punctuation symbols? (yes/no): ")
        disallowed = input("Characters that are not allowed (press Enter for none): ")
        password = generator.random_password(length, punctuation, disallowed)

    print(f"Generated password: {password}")
    print(f"Saved in the {password_type.title()} directory.")


if __name__ == "__main__":
    main()
