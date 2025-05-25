import random

words = ["messi", "ronaldo", "treika", "iniesta"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 7

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

while tries > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        tries -= 1
        print(f"Wrong! Tries left: {tries}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("Game over! The word was:", word)


