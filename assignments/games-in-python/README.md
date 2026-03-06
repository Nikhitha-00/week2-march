
# 🎮 Hangman Game

## 🎯 Objective
Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and user input by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 1. Game Setup
**Description:**
Set up your Python script to randomly select a word from a predefined list and initialize the game state.
**Requirements:**
- Create a list of at least 5 words
- Randomly select one word for each game
- Display underscores for each letter in the word (e.g., _ _ _ _)

### 2. Player Guess Loop
**Description:**
Implement the main game loop where the player guesses letters and the game updates the display.
**Requirements:**
- Prompt the player to guess a letter
- Reveal correctly guessed letters in their positions
- Track and display the number of incorrect guesses remaining
- Show the current progress after each guess

### 3. Game End Conditions
**Description:**
Handle win/lose scenarios and display appropriate messages.
**Requirements:**
- End the game when the word is fully guessed or attempts run out
- Display a congratulatory message for a win
- Show the correct word and a message if the player loses

#### Example Output
```text
Word: _ a _ _ _ a n
Guesses left: 3
Guess a letter: g
Word: _ a n g _ a n
Guesses left: 3
... (continues)
```
