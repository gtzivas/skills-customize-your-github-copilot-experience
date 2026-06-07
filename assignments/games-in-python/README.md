# 📘 Assignment: Games in Python

## 🎯 Objective

Build a text-based word guessing game in Python. In this assignment, you will practice loops, conditionals, strings, and user input while creating a playable Hangman-style experience.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the initial structure of the game by preparing a list of possible words, choosing one word for the current round, and setting the starting game state.

#### Requirements
Completed program should:

- Define a list of at least 5 possible secret words.
- Randomly choose one word from that list at the start of the game.
- Create variables to track guessed letters and remaining incorrect attempts.


### 🛠️ Player Turns and Game Outcome

#### Description
Implement the main game loop where the player guesses one letter at a time, sees progress, and either wins by guessing the word or loses when attempts run out.

#### Requirements
Completed program should:

- Prompt the player to enter one letter each turn.
- Show the current word progress using underscores for unguessed letters.
- Decrease remaining attempts only when the guess is incorrect.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts reach zero and reveal the word.
