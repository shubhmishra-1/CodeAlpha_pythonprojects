"""
CodeAlpha Python Programming Internship
Task 1: Hangman Game

A simple text-based Hangman game.
- Picks a random word from a predefined list
- Player guesses one letter at a time
- Game ends after 6 wrong guesses or when the word is fully revealed
"""

import random

WORDS = ["python", "hangman", "internship", "developer", "keyboard"]
MAX_WRONG_GUESSES = 6

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]


def choose_word():
    return random.choice(WORDS).lower()


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[wrong_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"Game over! You ran out of guesses. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
