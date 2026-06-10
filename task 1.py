import random
words = ["code", "alpha", "company", "hires", "interns"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
maximum_guesses = 6
print("Welcome to Hangman!")
while incorrect_guesses < maximum_guesses:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")
        print("Remaining chances:", maximum_guesses - incorrect_guesses)
if incorrect_guesses == maximum_guesses:
    print("\nGame Over!")
    print("The word was:", word)
