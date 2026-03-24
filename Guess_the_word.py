secret_word = 'tree'
def get_guess():
    attempts = 0
    while True:
        guess = input('Enter a guess: ')
        if len(guess) != 1 or not guess.islower():
            print('Your guess must be a single lowercase letter!')
        elif guess not in secret_word:
            print('That letter is not in the secret word!')
        else:
            print('That letter is in the secret word!')
            attempts += 1
            if attempts > 10:
                print('You have exceeded the maximum number of attempts!')
                break
            return guess

get_guess()


