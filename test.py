import random

def hangman():
    # Word list for the game
    words = ["python", "hangman", "developer", "programming", "challenge", "random"]
    
    # Select a random word
    word_to_guess = random.choice(words).lower()
    guessed_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    
    max_attempts = 6  # Set the limit on incorrect guesses
    attempts = 0

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("Word: ", " ".join(guessed_word))

    while attempts < max_attempts and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            # Reveal the letter(s) in the guessed word
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong! '{guess}' is not in the word.")
            attempts += 1

        # Display current progress
        print("Word: ", " ".join(guessed_word))
        print(f"Attempts left: {max_attempts - attempts}")

    # Check win or lose
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame Over! The word was:", word_to_guess)

# Run the game
if __name__ == "__main__":
    hangman()
