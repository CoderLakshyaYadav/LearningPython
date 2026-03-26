secret_word = "tree"

def update_dashes(secret_word, dashes, guess):
	result = ""
	for i in range(len(secret_word)):
		if secret_word[i] == guess:
			result += guess
		else:
			result += dashes[i]
	return result


def get_guess(secret_word, dashes):
	guessed_letters = set()
	guesses_left = 10

	while dashes != secret_word and guesses_left > 0:
		print(dashes)
		print(f"{guesses_left} incorrect guesses left.")

		guess = input("Guess: ").strip()

		if len(guess) != 1 or not guess.islower():
			print("Your guess must be a single lowercase letter!")
			continue

		if guess in guessed_letters:
			print("You already guessed that letter.")
			continue

		guessed_letters.add(guess)

		if guess in secret_word:
			print("That letter is in the word!")
			dashes = update_dashes(secret_word, dashes, guess)
		else:
			print("That letter is not in the word.")
			guesses_left -= 1

	if dashes == secret_word:
		print(dashes)
		print(f"Congrats! You win. The word was: {secret_word}")
	else:
		print(f"You lose. The word was: {secret_word}")


initial_dashes = "_" * len(secret_word)
get_guess(secret_word, initial_dashes)
