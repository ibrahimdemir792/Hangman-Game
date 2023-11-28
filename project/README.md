# Hangman Game
#### Video Demo:  https://youtu.be/oEtkdHW-0sg

#### Description
This Hangman game is an interactive console-based word-guessing game. It begins by prompting the player to select a game difficulty level between 3 and 10. The game then randomly selects a word of the specified length from a word generator library.

The player gets 6 attempts to guess the word by inputting individual letters. For each guess, the game checks if the letter exists in the chosen word. If the guessed letter is correct, it reveals its position in the word. Otherwise, it decrements the remaining attempts and displays the corresponding hangman stage.

The game continues until the player either correctly guesses the entire word or exhausts all attempts. Upon conclusion, it notifies the player of their win or loss, revealing the correct word if the player fails to guess it.

This console-based Hangman game engages players in word guessing and showcases their progress visually through ASCII art representations of hangman stages.

## Instructions

To play the game, run the `hangman.py` script. The game will start by asking difficulty level and displaying dashes representing each letter in the secret word. Guess letters one at a time and try to guess the word before running out of attempts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ibrahimdemir792/cs50p_final_project
## Project files
#### hangman_stages.py :
The get_hangman_stage() function generates ASCII art representing the hangman stages based on the remaining attempts. This function is crucial for visually rendering the hangman stages in the game. It returns ASCII representations of the hangman stages corresponding to the number of attempts remaining, showcasing the progressive stages of the hangman as the player guesses incorrectly.

This function provides visual feedback to the player, depicting the evolving hangman status throughout the game.

#### test_project.py :
This test suite validates the functionality of essential functions within a Hangman game. It uses Python's unittest.mock library to simulate user inputs and check the behaviors of functions in the game. The tests cover the following:

1. test_dashes(): Validates the generation of dash placeholders based on guessed letters.
2. test_guess_check(): Ensures correct checking of guessed letters against the target word.
3. test_guess_letter(): Simulates user input for letter guesses, testing input validation and lowercasing.

These tests confirm the reliability and accuracy of critical functions in the Hangman game.
