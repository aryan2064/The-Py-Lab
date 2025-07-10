import random

WORDS = ["python", "hangman", "computer", "science", "programming", "keyboard", "algorithm", "function"]
MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========="""
]


def get_display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("\n Welcome to Hangman!")
    print(f"Guess the word. You have {MAX_ATTEMPTS} attempts.\n")

    while attempts_left > 0:
        print(HANGMAN_STAGES[MAX_ATTEMPTS - attempts_left])
        print(f"\n  Word:  {get_display_word(word, guessed_letters)}")
        print(f"  Attempts left: {attempts_left}")

        if guessed_letters:
            correct = [l for l in guessed_letters if l in word]
            wrong = [l for l in guessed_letters if l not in word]
            if correct:
                print(f"  Correct guesses: {', '.join(correct)}")
            if wrong:
                print(f"  Wrong guesses:   {', '.join(wrong)}")

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[MAX_ATTEMPTS - attempts_left])
            print(f"\n  Word: {word}")
            print(f"\n  YOU WIN! You guessed the word: {word}")
            return True

    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print(f"\n  Game Over! The word was: {word}")
    return False



while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower().strip()
    if again != "y":
        print("Thanks for playing! Goodbye.\n")
        break
