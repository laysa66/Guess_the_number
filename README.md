# Guess the Number Game

A simple command-line "Guess the Number" game implemented in Python. The game generates a random number, and the player has to guess that number within a time limit. The game offers three difficulty levels with different time limits and number ranges.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Scoring](#scoring)

## Introduction

This Python script implements a text-based "Guess the Number" game. The player's objective is to guess the randomly generated secret number within a time limit. The game provides three difficulty levels, each with its own time limit and number range, offering players a challenging and fun experience.

The game uses ANSI escape codes for text colors to make the "TOO HIGH" and "TOO LOW" messages more noticeable, improving the user experience while playing.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or copy the Python code to a file (e.g., `guess_the_number.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:

```bash
python guess_the_number.py
```

## Game Rules
- Upon starting the game, the player is prompted to choose a difficulty level: Easy, Medium, or Hard.
- The game generates a random secret number within the specified number range for the chosen difficulty.
- The player has to guess the secret number within the given time limit. The remaining time is displayed after each guess.
- The game will inform the player if the guessed number is "TOO HIGH" or "TOO LOW" using different text colors for better visibility.
- If the player guesses the correct number within the time limit, they win the game and receive a score based on the number of attempts, time taken, and chosen difficulty level.
- The player can choose to play again after the game ends.

## Scoring
The player's score is calculated based on the following factors:

1. Number of attempts: A bonus score is awarded for making fewer attempts to guess the correct number.
2. Time taken: A bonus score is given for completing the game faster within the time limit.
3. Difficulty level: The score is adjusted based on the chosen difficulty level, with higher difficulty levels offering higher multipliers.

The game aims to provide an engaging experience by encouraging players to guess the correct number with fewer attempts and within the time limit to achieve higher scores.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
