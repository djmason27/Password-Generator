"""Generate 1,000 passwords with a randomly selected password type."""

import secrets

from password_generator import DEFAULT_WORD_LIST, PasswordGenerator


def main() -> None:
    generator = PasswordGenerator()
    counts = {"memorable": 0, "random": 0}

    for _ in range(1000):
        password_type = secrets.choice(("memorable", "random"))
        if password_type == "memorable":
            generator.memorable_password(
                number_of_words=secrets.choice((3, 4, 5)),
                available_cases=secrets.choice(("lower", "upper", "mixed")),
                word_list_path=DEFAULT_WORD_LIST,
            )
        else:
            generator.random_password(
                length=secrets.choice(range(12, 25)),
                include_punctuation=bool(secrets.randbelow(2)),
                disallowed_characters='"\'`\\',
            )
        counts[password_type] += 1

    print("Successfully generated and saved 1,000 passwords.")
    print(f"Memorable: {counts['memorable']}")
    print(f"Random: {counts['random']}")


if __name__ == "__main__":
    main()
