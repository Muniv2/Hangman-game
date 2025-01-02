# Usage
You can freely use, modify, and distribute this code. However, you must include the original copyright notice and this license in any copies or substantial portions of the software. The software is provided "as is," without any warranties or guarantees, and the author, Munir Tariq Malik (Muniv2), is not responsible for any issues that may arise.

## Hangman Game

This project is a simple Python implementation of the classic Hangman game. The game asks the user to enter a valid username and then randomly selects a country name from a predefined list. The user guesses the word by entering letters. The game provides feedback on correct and incorrect guesses and displays remaining chances. The game ends when the user either guesses the word correctly or runs out of attempts (6 wrong guesses).

### How It Works

1. **Username Validation:** The user is prompted to enter a valid username that contains only alphabets. If the input is invalid, the user is asked to try again.
2. **Word Selection:** A random country name is chosen from a list of countries (stored in `word_list`).
3. **Guessing Loop:** 
    - The game shows blanks for the unguessed letters in the country name.
    - The user guesses one letter at a time.
    - If the guess is correct, the letter is revealed in the word.
    - If the guess is incorrect, the user loses one of their 6 attempts.
4. **Game End:** 
    - If the user guesses the word correctly, a success message is shown.
    - If the user runs out of attempts (6 wrong guesses), the correct word is revealed, and the user loses the game.

### Features

- Randomly selects a country name for the user to guess.
- Tracks correct and incorrect guesses.
- Provides feedback on the remaining chances.
- Ends when the user guesses the word or runs out of attempts.
