import random

def play_hangman():
    # List of predefined words
    words = ["python", "developer", "hangman", "program", "code"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    tries = 6

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    # Game loop
    while tries > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
            print(f"❌ Wrong guess! Tries left: {tries}")

        print("Word:", " ".join(guessed_word))

    # Game result
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

def main():
    while True:
        play_hangman()
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break

# Run the game
main()
