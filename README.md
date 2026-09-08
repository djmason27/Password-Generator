# Password Generator

## Purpose

This Python project creates either memorable or random passwords. Every generated
password is automatically saved with its creation weekday, date, and time. The
project uses Python's `secrets` module instead of `random` for stronger password
generation.

## Files

- `password_generator.py` contains the generator class and interactive program.
- `generate_1000.py` demonstrates the program by generating 1,000 passwords,
  randomly choosing memorable or random for each password.
- `test_password_generator.py` contains automated tests.
- `sample_words.txt` is a small included word list so the project works immediately.
- `Memorable/Generated_Passwords.txt` is created for memorable-password history.
- `Random/Generated_Passwords.txt` is created for random-password history.

For the submitted version, download the assigned
`top_english_nouns_lower_100000.txt` file from Canvas, place it in this project
folder, and enter its path when prompted. You may also change `DEFAULT_WORD_LIST`
in `password_generator.py` to point to that file.

## How to Use

Python 3.10 or newer is recommended. From the project directory, run:

```bash
python password_generator.py
```

The program first asks for `memorable` or `random`.

### Memorable input

- Number of words (a positive integer)
- Available word cases: `lower`, `upper`, or `mixed`
- Path to a word-list text file, or Enter to use `sample_words.txt`

Example output: `forest4-RIVER2-cloud9`

Each selected word receives one random digit, and the pieces are joined by hyphens.

### Random input

- Password length (a positive integer)
- Whether punctuation should be included (`yes` or `no`)
- Any characters that must not appear, or Enter for none

Example output: `f8#Qv2!mLp7@`

### Output files

The program creates the required directories automatically. A saved line looks like:

```text
Tuesday, September 08, 2026 at 02:35:10 PM | forest4-RIVER2-cloud9
```

## Generate 1,000 Passwords

Run:

```bash
python generate_1000.py
```

The script randomly selects the password type for every iteration and appends all
1,000 results to the two history files.

## Run Tests

```bash
python -m unittest -v
```

## Libraries and Modules

Only modules from Python's built-in standard library are used. The project does
**not** use external or third-party libraries, and nothing needs to be installed
with `pip`:

- `secrets` — secure random selections
- `string` — character groups such as letters, digits, and punctuation
- `datetime` — creation timestamps
- `pathlib` — file and directory paths
- `tempfile`, `unittest`, and `re` — automated testing

## Generative AI Disclosure

Generative AI was used to help develop and test this project. The required chat
log is included in [`AI_CHAT_LOG.md`](AI_CHAT_LOG.md). Any additional AI use
should be added to that file before submission.

## GitHub Submission

1. Create a new **public** repository on GitHub.
2. Upload all project files, including `AI_CHAT_LOG.md`, the generated `Memorable` and `Random`
   directories and the course word list if your instructor permits redistribution.
3. Copy the repository URL and submit that link in Canvas.
