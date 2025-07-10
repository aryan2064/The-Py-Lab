# Hangman Game

A classic word-guessing game played in the terminal. Guess letters one at a time to reveal the hidden word before running out of attempts.

## Features

- 8 built-in words to guess
- 6 attempts before the hangman is fully drawn
- Visual hangman ASCII art that progresses with each wrong guess
- Tracks correct and wrong guesses
- Play again prompt after each round

## Requirements

- Python 3.x

No external dependencies required.

## How to Run

```bash
python hangman.py
```

## Example Output

```
 Guess the word. You have 6 attempts.


       -----
       |   |
           |
           |
           |
           |
    =========

  Word:  _ _ _ _ _ _ _ _ _
  Attempts left: 6

Enter a letter: h
Good guess! 'h' is in the word.

       -----
       |   |
           |
           |
           |
           |
    =========

  Word:  _ _ _ _ _ _ _ h _
  Attempts left: 6
  Correct guesses: h

Enter a letter: c
Wrong guess! 'c' is not in the word.

       -----
       |   |
       O   |
           |
           |
           |
    =========

  Word:  _ _ _ _ _ _ _ h _
  Attempts left: 5
  Correct guesses: h
  Wrong guesses:   c

Enter a letter: a
Good guess! 'a' is in the word.

       -----
       |   |
       O   |
           |
           |
           |
    =========

  Word:  a _ _ _ _ _ _ h _
  Attempts left: 5
  Correct guesses: h, a
  Wrong guesses:   c

Enter a letter: e
Wrong guess! 'e' is not in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a _ _ _ _ _ _ h _
  Attempts left: 4
  Correct guesses: h, a
  Wrong guesses:   c, e

Enter a letter: g
Good guess! 'g' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a _ g _ _ _ _ h _
  Attempts left: 4
  Correct guesses: h, a, g
  Wrong guesses:   c, e

Enter a letter: l
Good guess! 'l' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a l g _ _ _ _ h _
  Attempts left: 4
  Correct guesses: h, a, g, l
  Wrong guesses:   c, e

Enter a letter: o
Good guess! 'o' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a l g o _ _ _ h _
  Attempts left: 4
  Correct guesses: h, a, g, l, o
  Wrong guesses:   c, e

Enter a letter: r
Good guess! 'r' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a l g o r _ _ h _
  Attempts left: 4
  Correct guesses: h, a, g, l, o, r
  Wrong guesses:   c, e

Enter a letter: i
Good guess! 'i' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a l g o r i _ h _
  Attempts left: 4
  Correct guesses: h, a, g, l, o, r, i
  Wrong guesses:   c, e

Enter a letter: t
Good guess! 't' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word:  a l g o r i t h _
  Attempts left: 4
  Correct guesses: h, a, g, l, o, r, i, t
  Wrong guesses:   c, e

Enter a letter: m
Good guess! 'm' is in the word.

       -----
       |   |
       O   |
       |   |
           |
           |
    =========

  Word: algorithm

  YOU WIN! You guessed the word: algorithm

Play again? (y/n): n
Thanks for playing! Goodbye.
```