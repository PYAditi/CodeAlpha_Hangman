import random

# Step 1: List of predefined words
word_list = ["python", "hangman", "laptop", "flower", "coding"]
chosen_word = random.choice(word_list)

# Step 2: Game setup
guessed_word = ['_'] * len(chosen_word)
guessed_letters = []
max_attempts = 6
wrong_attempts = 0

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.\n")

# Step 3: Game Loop
while wrong_attempts < max_attempts and "_" in guessed_word:
    print("Current word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one valid letter.\n")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("❗ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        print("✅ Good guess!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
    else:
        # Wrong guess
        print("❌ Wrong guess!\n")
        wrong_attempts += 1
        print(f"Remaining attempts: {max_attempts - wrong_attempts}\n")

# Step 4: Game end
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
